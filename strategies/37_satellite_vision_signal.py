import numpy as np

def convolution_2d(image, kernel):
    k_h, k_w = kernel.shape
    img_h, img_w = image.shape
    
    output_h = img_h - k_h + 1
    output_w = img_w - k_w + 1
    
    new_image = np.zeros((output_h, output_w))
    
    for i in range(output_h):
        for j in range(output_w):
            region = image[i:i+k_h, j:j+k_w]
            new_image[i, j] = np.sum(region * kernel)
            
    return new_image

parking_lot = np.zeros((10, 10))
parking_lot[3:7, 3:7] = 1 
parking_lot[1, 1] = 1

kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

feature_map = convolution_2d(parking_lot, kernel)

car_count_score = np.sum(feature_map[feature_map > 0])
historical_avg = 15.0 
signal = "BUY" if car_count_score > historical_avg else "SELL"

print("--- SATELLITE PARKING LOT ANALYZER ---")
print("Input: Satellite Image Matrix (10x10 pixel)")
print(parking_lot)
print("\nFeature Map (After Convolution):")
print(feature_map.astype(int))
print("-" * 30)
print(f"Detected Activity Score: {car_count_score}")
print(f"Historical Baseline:     {historical_avg}")
print(f"Algo Signal:             {signal} WMT Stock")