import numpy as np
filename = input("Enter a class file to grade(i.e. class1 for class1.txt):")
VALID_ANSWER = ['A','B','C','D','']
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key_list = answer_key.split(',')

try:
  with open(filename + '.txt', 'r') as rf:
    print(f'Successfully opened {filename}')
    lines = 0
    invalid_lines = 0
    # lưu học sinh trả lời đúng
    student_scores = {}
    scores = []
    
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
      answers = line[10:].strip().split(',')
      if  len(valid_message) == 0 and  len(answers) != 25:
        valid_message = 'does not contain exactly 25 values'
      
      #Có phải tất cả câu trả lời là rỗng, hay abcd hay k
      valid_answers = all([ans for ans in answers if ans in VALID_ANSWER])
      if  len(valid_message) == 0 and not(valid_answers):
        valid_answers = 'contain invalid answers'

      #có valid_message thì xuất ra thông báo
      if len(valid_message) > 0:
        invalid_lines+=1
        print('Invalid line of data: ' + valid_message)
        print(line)
      else:
        score = 0
        for i in range(25):
          if answers[i] == answer_key_list[i]:
            score += 4
          elif answers[i] != answer_key_list[i] and answers[i] != '':
            score -=1
        student_id = line[0:9]
        student_scores[student_id] = score
        scores.append(score)
        
    if invalid_lines == 0:
      print('No errors found!')
    print('**** REPORT ****')
    print(f'Total valid lines of data: {lines - invalid_lines}')
    print(f'Total invalid lines of dada: {invalid_lines}')
    
    # tính điểm
    scores_arr = np.array(scores)
    scores_len = len(scores_arr)
    sorted_score_arr = np.sort(scores_arr)

    mean_score = np.round(np.mean(sorted_score_arr),2)
    max_score = np.max(sorted_score_arr)
    min_score = np.min(sorted_score_arr)
    range_score = max_score - min_score
    median_score = 0
    
    # nếu lẻ thì lấy ở giữa
    if scores_len % 2 != 0:
      middle_index = int((scores_len-1)/2)
      median_score = sorted_score_arr[middle_index]
    # nếu chẵn thì lấy trung bình của 2 phần tử ở giữa
    else:
      middle_index = int(scores_len/2)
      median_score = np.round((sorted_score_arr[middle_index]+sorted_score_arr[middle_index-1])/2, 2)
    #show scores
    print(f'Mean (average) score: {mean_score}')
    print(f'Highest score: {max_score}')
    print(f'Lowest score: {min_score}')
    print(f'Range of score: {range_score}')
    print(f'Median score: {median_score}')

    #write file
    with open(filename + '_grades.txt', 'w') as wf:
      for student in student_scores:
        wf.writelines(f'{student},{student_scores[student]}\n')
except FileNotFoundError:
  print('File cannot be found.')
except Exception as e:
  print('Exception Error', e)