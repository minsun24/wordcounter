from django.shortcuts import render

# Create your views here.
#메인 홈
def main(request):
  return render(request, 'index.html')
# 소개 페이지 
def about(request):
  return render(request,'about.html')

#결과 페이지 
def result(request):
  #text에 입력받은 데이터 담기 
  text = request.GET['text']
  #text의 공백으로 구분해 리스트 생성 
  text_list = text.split()
  
  #총 단어 수
  total = len(text_list) 
  
  #공백을 포함한 글자수 세기 
  text_with_blank = len(text)  
  
  #공백을 제외한 글자수 세기
  count = 0
  for i in text_list:
    count += len(i)
  text_without_blank = count
  # txt = text.replace(' ','').replace('\n','')
  # text_without_blank = len(txt)
  
  # text_= text.replace("\n", "")
  # text_without_blank = len(text_.replace(" ", ""))
  
  
  # 단어의 개수 세어주는 함수 - 딕셔너리 구조 key:value
  text_dict={}
  
  for word in text_list:
    if word in text_dict:
      text_dict[word] += 1
    else:
      text_dict[word] = 1  
      
  #단어 수 많이 나온 순서대로 정렬하기 
  words = sorted(text_dict.items(), key=lambda x:x[1], reverse=True)
  print(text_dict)
  
  
  #결과값 렌더링을 할 때 key:value값을 html에 보여주기 
  return render(request, 'result.html', {"words":words, 
                                         "total":total, 
                                         "text_without_blank":text_without_blank, 
                                         "text_with_blank":text_with_blank})
