# # Install the qr code and pillow libraries
# #   pip3 install "qrcode[pil]" in command line

# import qrcode

# qr = qrcode.QRCode(
#     version=1,
#     box_size=5,
#     border=10,
# )
# # image
# # data = 'https://www.duckduckgo.com'

# # call
# # phonenumber = 
# # data = f"tel:{phonenumber}"

# #  event

# def generate_event_qr_code(summary, dtstart, dtend, description, location, filename):
#     data = f"""BEGIN:VEVENT
#     SUMMARY:{summary}
#     DTSTART:{dtstart}
#     DTEND:{dtend}
#     DESCRIPTION:{description}
#     LOCATION:{location}
#     END:VEVENT"""

# generate_event_qr_code(
#     data = f"""BEGIN:VEVENT
#     summary='Tech support at barrstow village',
#     dtstart='20260318T100000Z',
#     dtend='20260318T110000Z',
#     location='Conference Room A',
#     description="Monthly project sync.",
#     filename='event_qr.png'
#     END:VEVENT"""
#     )

# qr.add_data(data)
# qr.make(fit=True)

# # save as image

# img = qr.make_image()
# img.save('qr-event.png')


import qrcode
from qrcode.constants import ERROR_CORRECT_H

def generate_event_qr_code(summary, dtstart, dtend, description, location, filename):
    """
    Generates a QR code with event details in iCalendar VEVENT format.

    :param summary: Event title (e.g., "Metallica Concert")
    :param dtstart: Start time in YYYYMMDDTHHMMSS format (e.g., "20260912T190000")
    :param dtend: End time in YYYYMMDDTHHMMSS format (e.g., "20260912T210000")
    :param description: Event description
    :param location: Event location
    :param filename: Output filename for the QR code image (e.g., "event_qr.png")
    """

    # The data string must be in the standard iCalendar VEVENT format
    event_data = f"""BEGIN:VEVENT
SUMMARY:{summary}
DTSTART:{dtstart}
DTEND:{dtend}
DESCRIPTION:{description}
LOCATION:{location}
END:VEVENT"""

    # Create the QR code instance
    # Using a high error correction level (H) is recommended for complex data
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(event_data)
    qr.make(fit=True)

    # Create the image and save it
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

# Example Usage:
generate_event_qr_code(
    summary="Team Meeting",
    dtstart="20260215T100000",
    dtend="20260215T110000",
    description="Discuss Q1 goals.",
    location="Conference Room A",
    filename="team_meeting_qr.png"
)