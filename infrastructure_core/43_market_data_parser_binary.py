import struct
import binascii

binary_packet = struct.pack('>cIII', b'S', 1234, 10500, 500)

print(f"--- HFT DATA PARSER ---")
print(f"Raw Binary Stream: {binascii.hexlify(binary_packet)}")
print("(This is what the network card sees. Humans can't read this.)")

def parse_packet(data):
    msg_type, stock_id, price_int, qty = struct.unpack('>cIII', data)
    
    msg_type = msg_type.decode('ascii')
    price = price_int / 100.0
    
    return {
        'Type': 'SYSTEM_EVENT' if msg_type == 'S' else 'UNKNOWN',
        'StockID': stock_id,
        'Price': price,
        'Qty': qty
    }

decoded = parse_packet(binary_packet)

print("\n--- DECODED OUTPUT ---")
print(f"Msg Type: {decoded['Type']}")
print(f"Stock ID: {decoded['StockID']}")
print(f"Price:    {decoded['Price']}")
print(f"Quantity: {decoded['Qty']}")

print("\nTier 1 Insight: Python Pandas takes ms to load. Struct takes ns (nanoseconds).")
print("HFT firms write this parser in C++ or FPGA.")