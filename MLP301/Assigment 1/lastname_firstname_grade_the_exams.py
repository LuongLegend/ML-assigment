filename = input("Enter a class file to grade(i.e. class1 for class1.txt):")
VALID_ANSWER = ['A','B','C','D','']

try:
  with open(filename + '.txt', 'r') as rf:
    print(f'Successfully opened {filename}')
    lines = 0
    invalid_lines = 0
    
    print('**** ANALYZING ****')
    for line in rf.readlines():
      lines+=1
      # Chỉ trả vễ lỗi đầu tiên gặp phải, khi xét dữ liệu từ trái sang phải
      # correct format: N#8 26 answers
      valid_message = ''
      num_list_index = [ i for i,num in enumerate(line) if num.isdigit()]

      #Không bắt đầu bằng N hoặc 8 ký tự sau N k phải tất cẩ đều là số
      if len(valid_message) == 0 and ( line[0] != 'N' or num_list_index != list(range(1, 9))): 
        valid_message = 'N# is invalid'
      
      # kiểm tra kết quả ký có đủ 26 câu trả lời hay k
      answers = line[9:].split(',')
      if  len(valid_message) == 0 and  len(answers) != 26:
        valid_message = 'does not contain exactly 26 values'
      
      #Có phải tất cả câu trả lời là rỗng, hay abcd hay k
      valid_answers = all([ans for ans in answers if ans in VALID_ANSWER])
      if  len(valid_message) == 0 and not(valid_answers):
        valid_answers = 'contain invalid answers'

      #có valid_message thì xuất ra thông báo
      if len(valid_message) > 0:
        invalid_lines+=1
        print('Invalid line of data: ' + valid_message)
        print(line)
        
    if invalid_lines == 0:
      print('No errors found!')
    print('**** REPORT ****')
    print(f'Total valid lines of data: {lines - invalid_lines}')
    print(f'Total invalid lines of dada: {invalid_lines}')    


except FileNotFoundError:
  print('File cannot be found.')
except Exception as e:
  print('Exception Error', e)