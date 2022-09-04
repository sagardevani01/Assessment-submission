#Calc
class StringCalculator:
    def add(self,numbers):
        if numbers=="":
            return 0
        else:
            #delim check
            delim = ','
            if numbers[:2] == "//":
                delim = numbers[2]
                numbers = numbers[4:]
            number_list = numbers.split(delim)
            
            #\n remove
            li = []
            for i in range(len(number_list)):
                num = number_list[i]
                if '\n' in num:
                    num = num.split('\n')
                    li.extend(num)
                    number_list[i] = '0'
            number_list.extend(li)
            
            #Calc Process
            negative_list = []
            for i in range(len(number_list)):
                number = number_list[i]
                if number>='a' and number<='z':
                    number_list[i] = ord(number)-96
                elif int(number)>1000:
                    number_list[i]=0
                elif int(number)<0:
                    negative_list.append(int(number))
                elif number>='0' and number<='9':
                    number_list[i] = int(number)
                    
            #Result
            if len(negative_list)>0:
                negative_list = [str(x) for x in negative_list]
                negative = " ".join(negative_list)
                raise Exception('Negatives not allowed '+negative)
            else:
                return sum(number_list)