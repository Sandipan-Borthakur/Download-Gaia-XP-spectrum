Download-Gaia-XP-spectrum

This code can be used to download Gaia XP spectrum from Vizier if available. You can either run the function from the terminal or you can import it in a python file. The 
Gaia spectrum wavelength is in nm and flux is in the units of $\rm W.\ m^{-2}.\ nm^{-1}$. This function converts the wavelength to $\rm Å$ and flux is saved in the units of $\rm ergs.\ s^{-1}. \ cm^{-2}. \ Å^{-1}$. 

| Conversion formula                                                         |
|----------------------------------------------------------------------------|
| $\rm 1\ W = 10^7\ ergs/s$                                                  |
| $\rm 1\ m^2 = 10^4\ cm^2$                                                  |
| $\rm 1\ nm = 10\ Å$                                                        |
| $\rm ergs.\ s^{-1}. \ cm^{-2}. \ Å^{-1} = 100 \times W.\ m^{-2}.\ nm^{-1}$ |

1. **Terminal** - 

   ```
   python3 download_gaia_spectrum "starname" "savepath"
2. **Python file** -

   ```
   from download_gaia_spectrum import download_gaia_spectrum
   starname = "HD 135446"`
   savepath = "savehere.txt"
   download_gaia_spectrum(starname = starname, savepath = savepath)
