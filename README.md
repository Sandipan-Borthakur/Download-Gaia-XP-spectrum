Download-Gaia-XP-spectrum

This code can be used to download Gaia XP spectrum from Vizier if available. You can either run the function from the terminal or you can import it in a python file.

1. Terminal - 

   python3 download_gaia_spectrum "starname" "savepath"

2. Python file -

   from download_gaia_spectrum import download_gaia_spectrum

   starname = "HD 135446"

   savepath = "savehere.txt"

   download_gaia_spectrum(starname = starname, savepath = savepath)
