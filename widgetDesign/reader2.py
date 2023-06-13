import usb.core
import usb.util

# Find the device connected to the USB port
dev = usb.core.find(idVendor=0x0c2e, idProduct=0x0989)

if dev is None:
    raise ValueError('Device not found')
else:
    print('Device found')
    print(dev)

# Set configuration of the device
dev.set_configuration()

# Get an endpoint instance
cfg = dev.get_active_configuration()
interface_number = cfg[(0,0)].bInterfaceNumber
alternate_setting = usb.control.get_interface(dev, interface_number)
intf = usb.util.find_descriptor(
    cfg, bInterfaceNumber = interface_number,
    bAlternateSetting = alternate_setting
)

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT
)

epIn = usb.util.find_descriptor(
    intf,
    # match the first IN endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_IN
)

assert ep is not None

# Read data from the scanner and print it out
while True:
    try:
        data = epIn.read(64)
        print(data)
    except usb.core.USBError as e:
        data = None
        if e.args == ('Operation timed out',):
            continue

