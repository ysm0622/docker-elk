import csv
locate = '../datas/hour_data/'
filenames = [f'd{i}_text_station_hour_2018_02.txt' for i in ['03', '04', '05', '06', '07', '08', '10', '11', '12']]
no_data_stations = ['315073','319153','317418']
with open('merged_data.csv', 'w') as csvout, open(f'{locate}d_meta.txt', 'r') as tsv:
	tsv = csv.reader(tsv, delimiter="\t")
	locate_dic = {}
	for row in tsv:
		locate_dic[row[0]] = f'{row[8]} {row[9]}'
	
	csvout = csv.writer(csvout)
	for filename in filenames:
		with open(locate+filename,'r') as tsvin:
			tsvin = csv.reader(tsvin, delimiter=',')

			for row in tsvin:
				if not row[1] in locate_dic.keys():
					continue
				row[18] = locate_dic[row[1]]
				# print(row[:19])
				csvout.writerow(row[:19])