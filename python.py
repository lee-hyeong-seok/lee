#json 모듈 불러오기
import json

#student.json = json파일의 변수
file_path = "./student.json"

#json 파일의 형태를 잡아주고 시작...
data={}
data['student'] = []

with open(file_path, 'w') as outfile:
    json.dump(data, outfile, indent=4)

#무한반복 루프문 
while True:
    a = input("회원가입: 1 로그인: 2 \n")
    
    # 1인경우 회원가입 : student에 dic형태로 담고
    if a == '1':
        def student():
            student ={}
            student['name'] = input('이름을 입력하세요 \n')
            student['age'] = input('나이를 입력하세요 \n')
            student['job'] = input('직업을 입력하세요 \n')
            student['id'] = input('id를 입력하세요 \n')
            student['passward'] = input('비밀번호를 입력하세요\n')
            return student
        #json 파일을 한번 읽어오고 python에서 인식할수있게 load 사용
        with open(file_path,'r') as json_file:
            json_data = json.load(json_file)


        #읽어온 json파일에 dic형태로 담은 student를 append하고
        json_data['student'].append(student())

        
        #json파일에 쓰기
        with open(file_path, 'w') as jfile:
            json.dump(json_data, jfile, indent=4)

    if a == '2':
        # with open(file_path,'r') as open_file:
        #     open_data = 

        break
    
    def student_name():
        with open(file_path,'r') as json_file_name:
            json_data_name = json.load(json_file_name)
            print(student['name'])


# with open(file_path, "r") as json_file:
#     json_data = json.load(json_file)

# json_data['student'].append(student())

# with open(file_path,'w') as jfile:
#     json.dump(json_data, jfile, indent=4)

