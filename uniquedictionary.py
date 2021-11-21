dict_list=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]

output_list = []
for i in range(len(dict_list)):
	if dict_list[i] not in dict_list[i + 1:]:
		output_list.append(dict_list[i])

# printing resultant list
print (output_list)

