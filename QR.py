import re
import numpy as np

class Element:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

def equation(a,b):#ax+b=0 형태의 a,b를 인수로 받는다.
    return -b/a #이때의 해 x = -b/a

division = re.compile('')
element_list = ['H', 'He', 'Li', 'Be','B','C','N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca','Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba',  'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra','Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c_alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number_list = ['0','1','2','3','4','5','6','7','8','9']
instant = True
# try:
#     with open('settings.txt', 'r') as f:
#         a = f.read()
#         if a == 'True':
#             pass
#         elif a == 'False':
#             instant = False
# except:pass
# print(instant)
print("""양적 관계를 자동으로 구해주는 프로그램입니다. 만든이 : 구일고 2학년(2022) 이현록 v1.0 2022-05-13

            1. 표기상 편의를 위해 아래첨자, 위첨자는 무시하고 작성합니다.
            Ex) H₂O -> H2O
            2. 이온 표현은 생략합니다.
            Ex) Na+ + Cl- -> Na + Cl
            3. 앙금반응식의 괄호표현은 풀어서 작성합니다.
            Ex) Cu(NO3)₂ -> CuN2O6
            4. 반응물, 생성물을 각각 입력하여 결과를 생성합니다.
            Ex) 반응물 : H2 + O2
            Ex) 생성물 : H2O
            Ex) 결과 : 2H2 + O2 -> 2H2O
            5. 작동이 멈춘 경우, Ctrl+C를 통해 처음 상태로 돌아갑니다.""")
            
while True:
    # try:
    #     a = int(input("""양적 관계를 자동으로 구해주는 프로그램입니다. 만든이 : 구일고 2학년(2022) 이현록 v0.0.1 2022-05-13
    #     # 1. 표기상 편의를 위해 아래첨자, 위첨자는 무시하고 작성합니다.
    #     # Ex) H₂O -> H2O
    #     # 2. 이온 표현은 생략합니다.
    #     # Ex) Na+ + Cl- -> Na + Cl
    #     # 3. 앙금반응식의 괄호표현은 풀어서 작성합니다.
    #     # Ex) Cu(NO3)₂ -> CuN2O6
    #     # 4. 반응물, 생성물을 각각 입력하여 결과를 생성합니다.
    #     # Ex) 반응물 : H2 + O2
    #     # Ex) 생성물 : H2O
    #     # Ex) 결과 : 2H2 + O2 -> 2H2O
    #     1. 반응물 작성
    #     실행할 명령을 입력하세요 : """))
    #     if a == 1:pass
    #     elif a == 2:
    #         ### 옵션 조정
    #         print('저장 완료.')
    #         continue
    #     else :
    #         print('에러. 잘못된 값 입력됨')
    #         continue
    # except:
    #     print('에러. 잘못된 값 입력됨')
    #     continue


    try:
        a = input("반응물 : ")
        #a = 'H2 + O2'
        
        reaction_element_list = []
        reaction_list = list(map(str.strip, a.split('+')))

        for i in range(len(reaction_list)):#이중 리스트 생성(화학식 개수만큼)
            reaction_element_list.append([])

        for i in reaction_list:
            for j in element_list:
                for m in re.finditer(j, i):
                    if  (m.start()+1 == len(i) and len(j)==1) or (m.start()+2==len(i) and len(j) == 2):#마지막 원소
                        #print('le')
                        reaction_element_list[reaction_list.index(i)].append(Element(j,1))
                        continue
                    if i[m.start()+1] in alphabet_list and len(j) == 2:#2글자 원소
                        #print('2e')
                        try:
                            n = ''
                            c = 2
                            int(i[m.start()+c])
                            while True:
                                try:
                                    int(i[m.start()+c])
                                    n+=i[m.start()+c]
                                    c+=1
                                except:break
                            #int(i[m.start()+c])
                            reaction_element_list[reaction_list.index(i)].append(Element(j, n))
                        except:
                            reaction_element_list[reaction_list.index(i)].append(Element(j, 1))
                        continue
                    if (i[m.start()+1] in number_list or i[m.start()+1] in c_alphabet_list) and len(j) == 1:#1글자 원소
                        try:
                            n = ''
                            c = 1
                            int(i[m.start()+c])
                            while True:
                                try:
                                    int(i[m.start()+c])
                                    n+=i[m.start()+c]
                                    #print(n)
                                    c+=1
                                except:break
                            #int(i[m.start()+c])
                            #print(i[m.start()+1:m.start()+n])
                            reaction_element_list[reaction_list.index(i)].append(Element(j, n))
                        except:
                            reaction_element_list[reaction_list.index(i)].append(Element(j, 1))
                        continue
        run=True
        while run:
            run = False
            for i in reaction_element_list:
                a = []
                b = []
                c = []
                for j in i:
                    if j.name in a:
                        s = a.index(j.name)
                        q = str(int(b[s])+int(j.amount))
                        r = i
                        r.remove(j)
                        r.remove(c[a.index(j.name)])
                        r.append(Element(j.name, q))
                        reaction_element_list[reaction_element_list.index(i)] = r
                        run = True
                        break
                    a.append(j.name)
                    b.append(j.amount)
                    c.append(j)
                    #print(j.name, j.amount)



        b = input("생성물 : ")
        #b = 'H2O'
        product_element_list = []
        product_list = list(map(str.strip, b.split('+')))

        for i in range(len(product_list)):#이중 리스트 생성(화학식 개수만큼)
            product_element_list.append([])

        for i in product_list:
            for j in element_list:
                for m in re.finditer(j, i):
                    if m.start()+1==len(i) or (m.start()+2==len(i) and len(j) == 2):#마지막 원소
                        product_element_list[product_list.index(i)].append(Element(j,1))
                        continue
                    if i[m.start()+1] in alphabet_list and len(j) == 2:#2글자 원소
                        
                        try:
                            n = ''
                            c = 2
                            int(i[m.start()+c])
                            while True:
                                try:
                                    int(i[m.start()+c])
                                    n+=i[m.start()+c]
                                    c+=1
                                except:break
                            #int(i[m.start()+c])
                            product_element_list[product_list.index(i)].append(Element(j, n))
                        except:
                            product_element_list[product_list.index(i)].append(Element(j, 1))
                        continue
                    if (i[m.start()+1] in number_list or i[m.start()+1] in c_alphabet_list) and len(j) == 1:#1글자 원소
                        try:
                            n = ''
                            c = 1
                            int(i[m.start()+c])
                            while True:
                                try:
                                    int(i[m.start()+c])
                                    n+=i[m.start()+c]
                                    c+=1
                                except:break
                            #int(i[m.start()+c])
                            product_element_list[product_list.index(i)].append(Element(j, n))
                        except:
                            product_element_list[product_list.index(i)].append(Element(j, 1))
                        continue

        for i in product_element_list:
            for j in i:pass
                #print(j.name, j.amount)
        run=True
        cnt=0
        while run:
            run = False
            for i in product_element_list:
                a = []
                b = []
                c = []
                for j in i:
                    if j.name in a:
                        s = a.index(j.name)
                        q = str(int(b[s])+int(j.amount))
                        r = i
                        r.remove(j)
                        r.remove(c[a.index(j.name)])
                        r.append(Element(j.name, q))
                        product_element_list[product_element_list.index(i)] = r
                        run = True
                        break
                    a.append(j.name)
                    b.append(j.amount)
                    c.append(j)
                    #print(j.name, j.amount)
        
        unknown_list = [[],[]]
        for i in range(len(reaction_list)):
            unknown_list[0].append(-1)
        for i in range(len(product_list)):
            unknown_list[1].append(-1)


        #양적관계 식 작성
        using_element_list = []
        for i in range(len(reaction_element_list)):
            for j in range(len(reaction_element_list[i])):
                # print(i, j)
                if (reaction_element_list[i][j].name in using_element_list) == False:
                    using_element_list.append(reaction_element_list[i][j].name)
        
        equation_list = []
        for i in range(len(using_element_list)):
            equation_list.append([])
            for j in reaction_element_list:
                for m in j:
                    if m.name == using_element_list[i]:
                        equation_list[i].append(int(m.amount))
                        r=True
                        break
                    else: pass
                if r==True:
                    r=False
                else:
                    equation_list[i].append(0)

            for j in product_element_list:
                for m in j:
                    if m.name == using_element_list[i]:
                        #print(m.amount)
                        equation_list[i].append(int(m.amount))
                        r=True
                        break
                    else: pass
                if r==True:
                    r=False
                else:
                    equation_list[i].append(0)
        #print(equation_list)
        # print(equation_list)
        # print(product_element_list)
        # print(reaction_element_list)##clear!!!!
        # print(unknown_list)
        #양적관계 식 풀이 - 미완 난이도 상

        # 일단 미지수2개의 식중 하나의 값을 1로 정한다.
        for i in equation_list:
            cnt = 0
            first = True
            location = 0
            for j in range(len(i)):
                if i[j] != 0:
                    if first == True:
                        first = False
                        location = j
                    cnt+=1
            if cnt == 2:break
        unknown_list[0][location] = 1#미지수 가정
        unknown_list = unknown_list[0] + unknown_list[1]
        #print(unknown_list)
        # print(unknown_list)
        #이후 미지수를 줄인다.
        running = True
        while running:
            if cnt>100:
                raise 'error'
            for i in equation_list:
                cnt = 0#미지수 카운터
                unt = 0#모르는 미지수 카운터
                first = True
                fl = 0#첫째 위치
                ll = 0#마지막 위치
                for j in range(len(i)):
                    if i[j] != 0:
                        cnt +=1
                        if unknown_list[j] != -1 and first==True:
                            first = False
                            fl = j
                        if unknown_list[j] == -1:
                            unt+=1
                            ll = j
                if cnt == 2 and unt == 1:
                    # print(fl, ll, unknown_list)
                    # print(equation_list[equation_list.index(i)][ll],-equation_list[equation_list.index(i)][fl]*unknown_list[fl])
                    #unknown_list[ll] = equation(equation_list[equation_list.index(i)][fl],equation_list[equation_list.index(i)][ll])
                    unknown_list[ll] = equation(equation_list[equation_list.index(i)][ll], -equation_list[equation_list.index(i)][fl]*unknown_list[fl])
                    #print(unknown_list)

                elif cnt>2 and unt == 1:#모르는 미지수
                    const = 0 #상수
                    for j in range(len(i)):
                        if unknown_list[j] == -1:continue
                        if j> len(reaction_list)-1:#반응물이면,
                            const-=equation_list[equation_list.index(i)][j]*unknown_list[j]
                        else:
                            const+=equation_list[equation_list.index(i)][j]*unknown_list[j]
                        #print(const)
                    coe = equation_list[equation_list.index(i)][ll]
                    #print(coe)
                    if ll>len(reaction_list):
                        coe *= -1
                    unknown_list[ll] = equation(coe,const)
                        
                    # print(fl, ll, unknown_list, 'nn')
                    
            for i in range(len(unknown_list)):
                if unknown_list[i] == -1:break
                elif i == len(unknown_list)-1 : running = False

        # 미지수를 줄이는 과정으로. 미지수 (n개)가 같은 식이 n개 있다면 연립방정식으로 계산하여 구현한다.(일단은 n=2만) .. 행렬 들어가니 참고. 아직은 구현x
    
        # 이후 미지수의 값들이 다 정해지면 세 미지수가 정수가 될때까지 수를 곱하여 간단한 정수비로 나타낸다.
        cnt = 0
        e=False
        running = True
        while running:
            if cnt>100:
                raise 'error'
            temp = []
            cnt+=1
            for i in unknown_list:
                temp.append(i*cnt)
            for j in range(len(temp)):
                if temp[j] == int(temp[j]):
                    if j == len(temp)-1:e=True
                    continue
                else : break
            if e==True:running = False
        answer = []
        for i in temp:
            if int(i) == 1:answer.append('')
            else: answer.append(int(i))
        cnt = 0
        for i in reaction_list+product_list:
            print(str(answer[cnt])+i, end='')
            if cnt == len(reaction_list)-1: print(' -> ', end='')
            elif not (cnt == len(answer)-1):print(' + ',end='')
            cnt += 1
        print('\n\n\n')
    except:
        print('에러 발생. 잘못된 값이 입력되었습니다.')
    #최종 결과 작성