# importing Image class from PIL package
from PIL import Image

# some will expand fill the row(if using height)
# the image resize needs to be a little bigger (+3?)
MAX_SIZE = (100000, 153)

files = ['100_2563.jpg', '2013-05-21 19.32.41.jpg', '2013-07-29 08.44.02.jpg', '232323232-fp54377-nu=3896-239-783-298723987423-ot1lsi.jpg', '232323232-fp54434-nu=3896-239-74;-298723983-23-ot1lsi.jpg', '73370289297__778C85B2-23C0-4B94-A9B2-D873318BC341.JPEG', 'dsc00011.jpg', 'dsc_0495.jpg', 'dsc_0949.jpg', 'DSC_0972.JPG', 'IMG_0007.JPEG', 'IMG_0008.JPG', 'IMG_0012.JPG', 'IMG_0018.JPG', 'IMG_0049.JPG', 'IMG_0050.JPG', 'IMG_0051.JPG', 'IMG_0103.JPG', 'IMG_0166.JPG', 'IMG_0206.JPG', 'IMG_0280.JPG', 'IMG_0381.JPG', 'IMG_0382.JPG', 'IMG_0383.JPG', 'IMG_0384.JPG', 'IMG_0401.JPG', 'IMG_0426.JPG', 'IMG_0427.JPG', 'IMG_0465.JPG', 'IMG_0466.JPG', 'IMG_0467.JPG', 'IMG_0528.JPG', 'IMG_0529.JPG', 'IMG_0530.JPG', 'IMG_0531.JPG', 'IMG_0532.JPG', 'IMG_0537.JPG', 'IMG_0538.JPG', 'IMG_0539.JPG', 'IMG_0540.JPG', 'IMG_0541.JPEG', 'IMG_0542.JPG', 'IMG_0551.JPG', 'IMG_0552.JPG', 'IMG_0598.JPG', 'IMG_0711.JPG', 'IMG_0716.JPG', 'IMG_0717.JPG', 'IMG_0868.JPG', 'IMG_0943.JPG', 'IMG_0957.JPG', 'IMG_0958.JPG', 'IMG_0959.JPG', 'IMG_0960.JPG', 'IMG_0961.JPG', 'IMG_0962.JPG', 'IMG_0963.JPG', 'IMG_0978.JPG', 'IMG_0992.JPEG', 'IMG_1029.JPG', 'IMG_1030.JPG', 'IMG_1031.JPG', 'IMG_1032.JPG', 'IMG_1034.JPG', 'IMG_1037.JPG', 'IMG_1041.JPG', 'IMG_1042.JPG', 'IMG_1046.JPG', 'IMG_1067.JPG', 'IMG_1071.JPG', 'IMG_1072.JPG', 'IMG_1074.JPG', 'IMG_1075.JPG', 'IMG_1076.JPG', 'IMG_1079.JPG', 'IMG_1081.JPG', 'IMG_1082.JPG', 'IMG_1083.JPG', 'IMG_1084.JPG', 'IMG_1086.JPG', 'IMG_1087.JPG', 'IMG_1088.JPG', 'IMG_1090.JPG', 'IMG_1231.JPG', 'IMG_1259.JPEG', 'IMG_1260.JPG', 'IMG_1474-1.JPG', 'IMG_1474.JPG', 'IMG_1522.JPG', 'IMG_1649.JPG', 'IMG_1650.JPG', 'IMG_1651.JPG', 'IMG_1662.JPG', 'IMG_1663.JPG', 'IMG_1675.JPG', 'IMG_1681.JPG', 'IMG_1682.JPG', 'IMG_1683.PNG', 'IMG_1809-1.JPG', 'IMG_1809.JPG', 'IMG_1810-1.JPG', 'IMG_1810.JPG', 'IMG_1816.JPG', 'IMG_1817.JPG', 'IMG_1831.PNG', 'IMG_1842-1.JPG', 'IMG_1842.JPG', 'IMG_1925.JPG', 'IMG_1926.JPG', 'IMG_1927.JPG', 'IMG_1928.JPG', 'IMG_1929.JPG', 'IMG_1930.JPG', 'IMG_1931.JPG', 'IMG_1932.JPG', 'IMG_1933.JPG', 'IMG_1934.JPG', 'IMG_1935.JPG', 'IMG_2002.JPG', 'IMG_2006.JPG', 'IMG_2056.JPG', 'IMG_2090.JPG', 'IMG_2112.JPG', 'IMG_2113.JPG', 'IMG_2114.JPG', 'IMG_2115.JPG', 'IMG_2116.PNG', 'IMG_2164.PNG', 'IMG_2307.JPG', 'IMG_2309.JPG', 'IMG_2325.JPG', 'IMG_2326.JPG', 'IMG_2326.PNG', 'IMG_2327.PNG', 'IMG_2328.PNG', 'IMG_2395.JPG', 'IMG_2539.JPG', 'IMG_2540.JPG', 'IMG_2541.JPG', 'IMG_2542.JPG', 'IMG_2665.JPEG', 'IMG_2791.JPG', 'IMG_2850.JPEG', 'IMG_2852.JPG', 'IMG_2884.JPEG', 'IMG_2933.JPG', 'IMG_2934.JPG', 'IMG_2935.JPG', 'IMG_2936.JPG', 'IMG_2937.JPG', 'IMG_2938.JPG', 'IMG_2939.JPG', 'IMG_2941.JPG', 'IMG_2942.JPG', 'IMG_2943.JPG', 'IMG_2944.JPG', 'IMG_3007.JPG', 'IMG_3307.JPG', 'IMG_3372.JPG', 'IMG_3415.JPG', 'IMG_3522.JPEG', 'IMG_3523.JPEG', 'IMG_3524.JPEG', 'IMG_3525.JPEG', 'IMG_3528.JPEG', 'IMG_3529.JPG', 'IMG_3530.JPEG', 'IMG_3531.PNG', 'IMG_3532.PNG', 'IMG_3609.JPG', 'IMG_3861.JPG', 'IMG_3885.JPEG', 'IMG_3894.JPEG', 'IMG_3895.JPEG', 'IMG_4026.JPG', 'IMG_4151.JPG', 'IMG_4152.JPG', 'IMG_4234.JPG', 'IMG_4303-1.JPG', 'IMG_4303.JPG', 'IMG_4304.JPG', 'IMG_4425.JPG', 'IMG_4429.PNG', 'IMG_4490.JPG', 'IMG_4630.JPEG', 'IMG_4631.JPEG', 'IMG_4632.JPEG', 'IMG_4633.JPEG', 'IMG_4634.JPEG', 'IMG_4635.JPEG', 'IMG_4636.JPEG', 'IMG_4877.JPEG', 'IMG_4878.JPG', 'IMG_4972.JPG', 'IMG_5075.JPG', 'IMG_5086.JPEG', 'IMG_5102.PNG', 'IMG_5160.JPG', 'IMG_5239.JPG', 'IMG_5241.JPG', 'IMG_5263.JPG', 'IMG_5264.JPG', 'IMG_5265.JPG', 'IMG_5266.JPG', 'IMG_5273.JPG', 'IMG_5567.JPG', 'IMG_5568.JPG', 'IMG_5569.JPG', 'IMG_5570.JPG', 'IMG_5573.JPG', 'IMG_5574.JPG', 'IMG_5575.JPG', 'IMG_5576.JPG', 'IMG_5577.JPG', 'IMG_5578.JPG', 'IMG_5579.JPG', 'IMG_5580.JPEG', 'IMG_5746.JPEG', 'IMG_5801.JPG', 'IMG_5802.PNG', 'IMG_6019.JPG', 'IMG_6020.JPG', 'IMG_6025.JPG', 'IMG_6026.JPG', 'IMG_6057.JPG', 'IMG_6063.JPG', 'IMG_6064.JPG', 'IMG_6065.JPG', 'IMG_6066.JPG', 'IMG_6067.JPG', 'IMG_6068.JPG', 'IMG_6069.JPG', 'IMG_6070.JPG', 'IMG_6071.JPG', 'IMG_6072.JPG', 'IMG_6073.JPG', 'IMG_6075.JPG', 'IMG_6076.JPG', 'IMG_6083.JPG', 'IMG_6084.JPG', 'IMG_6085.JPG', 'IMG_6123.JPG', 'IMG_6124.JPG', 'IMG_6131.JPG', 'IMG_6134.JPG', 'IMG_6135.JPG', 'IMG_6136.JPG', 'IMG_6138.JPG', 'IMG_6139-1.JPG', 'IMG_6139.JPG', 'IMG_6140.JPG', 'IMG_6142.JPG', 'IMG_6148.JPG', 'IMG_6152.JPG', 'IMG_6155.JPEG', 'IMG_6155.JPG', 'IMG_6166.JPG', 'IMG_6168.JPG', 'IMG_6171.JPEG', 'IMG_6172.JPEG', 'IMG_6173.JPEG', 'IMG_6174.JPEG', 'IMG_6175.JPEG', 'IMG_6178.MP4', 'IMG_6179.JPEG', 'IMG_6180.JPEG', 'IMG_6181.JPEG', 'IMG_6182.JPEG', 'IMG_6183.JPEG', 'IMG_6184.JPEG', 'IMG_6184.JPG', 'IMG_6185.JPEG', 'IMG_6189.JPG', 'IMG_6194.JPG', 'IMG_6199.JPG', 'IMG_6220.JPG', 'IMG_6223.JPG', 'IMG_6224.JPG', 'IMG_6225.JPG', 'IMG_6313.JPG', 'IMG_6320.JPEG', 'IMG_6321.JPEG', 'IMG_6324.MP4', 'IMG_6326.JPEG', 'IMG_6327.JPEG', 'IMG_6328.JPEG', 'IMG_6329.JPEG', 'IMG_6330.JPEG', 'IMG_6331.JPEG', 'IMG_6332.JPEG', 'IMG_6333.JPEG', 'IMG_6334.JPEG', 'IMG_6335.JPEG', 'IMG_6336.JPEG', 'IMG_6337.JPEG', 'IMG_6338.JPEG', 'IMG_6339.JPEG', 'IMG_6340.JPEG', 'IMG_6343.JPEG', 'IMG_6444.JPEG', 'IMG_6551.JPG', 'IMG_6692.JPG', 'IMG_6693.JPG', 'IMG_6694.JPG', 'IMG_6697.JPEG', 'IMG_6698.JPEG', 'IMG_6700.JPG', 'IMG_6701-1.JPG', 'IMG_6701.JPG', 'IMG_6702.JPG', 'IMG_6703.JPG', 'IMG_6704.JPEG', 'IMG_6708.JPG', 'IMG_6719.JPG', 'IMG_6720.JPG', 'IMG_6721.JPG', 'IMG_6722.JPG', 'IMG_6723.JPG', 'IMG_6724.JPG', 'IMG_6726.JPG', 'IMG_6727.JPG', 'IMG_6728.JPG', 'IMG_6729.JPG', 'IMG_6733.JPEG', 'IMG_6734.JPEG', 'IMG_6737.JPG', 'IMG_6737.MOV', 'IMG_6738.JPG', 'IMG_6738.MOV', 'IMG_6739.JPG', 'IMG_6739.MOV', 'IMG_6740.JPG', 'IMG_6740.MOV', 'IMG_6741.JPG', 'IMG_6741.MOV', 'IMG_6742.JPG', 'IMG_6742.MOV', 'IMG_7030.JPG', 'IMG_7031.JPEG', 'IMG_7081.JPEG', 'IMG_7082.JPEG', 'IMG_7118.PNG', 'IMG_7130.JPG', 'IMG_7212.JPG', 'IMG_7298.JPG', 'IMG_7301.JPEG', 'IMG_7302.JPEG', 'IMG_7303.JPEG', 'IMG_7307.JPEG', 'IMG_7308.JPEG', 'IMG_7310.JPEG', 'IMG_7312.JPEG', 'IMG_7313.JPEG', 'IMG_7314.JPEG', 'IMG_7315.JPEG', 'IMG_7316.JPEG', 'IMG_7364.heic.JPG', 'IMG_7364.JPEG', 'IMG_7553.MP4', 'IMG_7559.JPG', 'IMG_7560.JPEG', 'IMG_7567.JPEG', 'IMG_7567.MOV', 'IMG_7569.JPEG', 'IMG_7569.MOV', 'IMG_7570.JPEG', 'IMG_7570.MOV', 'IMG_7571.JPEG', 'IMG_7571.MOV', 'IMG_7579.MP4', 'IMG_7582.JPEG', 'IMG_7582.MOV', 'IMG_7583.JPEG', 'IMG_7583.MOV', 'IMG_7630.JPG', 'IMG_8018.JPG', 'IMG_8019.JPEG', 'IMG_8058.JPG', 'IMG_8059.JPG', 'IMG_8060.JPG', 'IMG_8247.JPG', 'IMG_8979.JPEG', 'IMG_8980.JPEG', 'IMG_8984.JPEG', 'IMG_8985.JPEG', 'IMG_8990.JPEG', 'IMG_8991.JPEG', 'IMG_8992.JPEG', 'IMG_8995.JPEG', 'IMG_8996.JPEG', 'IMG_8997.JPG', 'IMG_8999.JPEG', 'IMG_9001.JPEG', 'IMG_9002.JPEG', 'IMG_9003.JPEG', 'IMG_9005.JPG', 'IMG_9006.JPG', 'IMG_9007.JPG', 'IMG_9008.JPG', 'IMG_9009.JPG', 'IMG_9011.MP4', 'IMG_9013.JPEG', 'IMG_9014.JPEG', 'IMG_9015.JPEG', 'IMG_9016.JPEG', 'IMG_9017.JPEG', 'IMG_9018.JPEG', 'IMG_9019.MP4', 'IMG_9020.JPEG', 'IMG_9021.JPEG', 'IMG_9061.JPG', 'IMG_9062.JPG', 'IMG_9063.JPG', 'IMG_9067.JPG', 'IMG_9068.JPG', 'IMG_9069.JPG', 'IMG_9070.JPG', 'IMG_9071.JPG', 'IMG_9392.JPG', 'IMG_9577.JPEG', 'IMG_9578.JPEG', 'IMG_9579.JPEG', 'IMG_9580.JPEG', 'IMG_9581.JPG', 'IMG_9582.JPEG', 'IMG_9583.JPEG', 'IMG_9584.JPEG', 'IMG_9585.JPEG', 'IMG_9586.JPEG', 'IMG_9587.JPEG', 'IMG_9588.JPEG', 'IMG_9589.JPEG', 'IMG_9590.JPEG', 'IMG_9592.JPEG', 'IMG_9593.JPEG', 'IMG_9753.JPG', 'IMG_9754.JPG', 'IMG_9755.JPG', 'IMG_9756.JPG', 'IMG_9757.JPG', 'IMG_9814.JPG', 'Resized_Resized_20220526_120024.jpeg', 'Resized_Resized_20230402_160031.jpeg', 'Resized_Resized_20230402_160038.jpeg', 'result.mp4']



for file in files:
	ext = file[len(file) - 3:].upper()
	if ext != 'MOV' and ext != 'MP4':
		image = Image.open(file)
		image.thumbnail(MAX_SIZE)
		image.save("thumbs/t" + file)

