def main():
    scores = [[78,45,70,59], [33,80,56,47], [54,20,67]]
    for index,score in enumerate(scores):
        for inner_index,inner_value in enumerate(score):
           # print(f"inner value: ", inner_value)
        #    print(f"inner list: ", score[index])
          #  print(f"inner value wih index: ", score[inner_index])

            print(f"inner value: ", inner_value, end='\t')
            print(f"inner index: ", inner_index)

            print(f"inner list : ", score, end='\t')
            print(f"inner list index: ", index)

def days_month():
    days_per_month = {'january': 31, 'feburay': 28, 'march': 31}
    for month_name in days_per_month.keys():
        print(f"month name: ", month_name, end="")


if __name__ == '__main__':
    main()
