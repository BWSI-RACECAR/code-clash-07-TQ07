class Solution:
    def count_XO(self, string):
            #type string: string
            #return type: boolean
            x = 0
            o = 0
            #TODO: Write code below to returnn a boolean value with the solution to the prompt.
            for s in string:
                if s == "X":
                    x = x+1
                if s == "O":
                    o = o + 1
            if x == o:
                 return True
            else:
                 return False
            pass
                
def main():
    input1=input()
    tc1 = Solution()
    ans = tc1.count_XO(input1)
    print(ans)

if __name__ == "__main__":
    main()
