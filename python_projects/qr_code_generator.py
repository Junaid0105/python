#import inbuilt module for qr generation
import qrcode as qr

# make is a function to create qr code of any link or text
linkedin_qr = qr.make("https://www.linkedin.com/in/junaid-alam-53b712178/")

#after create qr, we need to save it
linkedin_qr.save("juniad_linkedin_qr.png")

