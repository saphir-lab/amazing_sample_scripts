import wifi_qrcode_generator as qr
qr_code = qr.wifi_qrcode('wifi name ', False, 'WPA', 'password')
qr_code.print_ascii()
# qr_code.make_image().save('qr.png')