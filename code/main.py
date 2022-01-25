from labjack import ljm

def main():
	labjack_product = "T4"
	labjack_ip = "192.168.171.6" # found via Kipling Software ran on machine on network

	# Open a specific LabJack
	handle = ljm.openS("ANY", "ANY", labjack_ip)

	# Call eReadName to read the serial number from the LabJack.
	name = "SERIAL_NUMBER"
	result = ljm.eReadName(handle, name)

	print(f"\neReadName result: ")
	print(f"    {name} = {int(result)}")

if __name__ == '__main__':
	main()