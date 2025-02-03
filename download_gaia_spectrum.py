from astroquery.vizier import Vizier
from astropy.coordinates import Angle
from astropy.io import ascii
import sys

def download_gaia_spectrum(starname,savepath):
    # Enable all columns (including XP sampled spectra)
    Vizier.ROW_LIMIT = -1
    Vizier.TIMEOUT = 300  # Increase timeout if needed

    # Query I/355/gaiadr3 for XP sampled spectra availability (XPsamp flag)
    catalog = "I/355/xpsample"
    query = Vizier(columns=["lambda","Flux","e_Flux"],column_filters={"XPsamp":">0"}, catalog=catalog)
    result = query.query_object(starname, radius=Angle(0.003, "deg"))

    # Check if the source has XP sampled spectra
    if result and len(result[catalog]) > 0:
        data = result[catalog]
        data['lambda'] = data['lambda']*10
        data['Flux'] = data['Flux']*100
        data['e_Flux'] = data['e_Flux']*100
        ascii.write(result[catalog], savepath, names=["Wave","Flux","Fluxerr"],formats={"Wave":"%.f","Flux":"%.7e","Fluxerr":"%.7e"}, overwrite=True)
    else:
        print(f"Source {starname} not found in VizieR Gaia catalog I/355/xpsample.")

if __name__=="__main__":
    try:
        starname,savepath = sys.argv[1],sys.argv[2]
        download_gaia_spectrum(starname=starname,savepath=savepath)
    except:
        NotImplementedError("Code did not find Gaia xp spectrum. Check the catalog: I/355/xpsample in Vizier.")