class Bookyourmovie:
    def __init__(self):
    
        print('WELCOME TO BOOKYOURMOVIE.COM!!!')
        print('Wear Mask properly')
        print('Keep good hygine :)')
    
    
        self.r = input('Enter The Number Of Rows :')
        self.c = input('Enter The Number Of seats in each row :')
    
    
        self.s=[0]*int(self.r)
        self.t=[' ']+[str(i+1) for i in range(int(self.c))]
        for i in range(int(self.r)):
            self.s[i]=[str(i+1)]+['S']*int(self.c)
        
        
        if int(self.r)*int(self.c) <=60:
            self.totalincome=10*int(self.r)*int(self.c)
        if int(self.r)*int(self.c) >=60:
            if int(self.r)%2==0:
                self.totalincome=9*int(self.c)
            else:
                f=(int(self.r)//2)
                self.totalincome = (8*f*int(self.c))+(10*(int(self.r)-f)*int(self.c))
            
            
            
        self.currentincome=0
        self.userinfo = {}
        self.options()
            
        
        
    def options(self):
        print('\n')
        print('Plz select from the below option')
        print('1.Show the seats')
        print('2.Buy a ticket')
        print('3.Statistics')
        print('4.Show_booked_ticket_userinfo ')
        print('0.Exit')
        print('Please Type Corresponding Number For Corresponding Option')
        print('****** ****** *****')
    
    
        x= input()
        if x=='1':
            self.showtickets()
        elif x=='2':
            self.buyticket()
        elif x=='3':
            self.statistics()
        elif x=='4':
            self.show_booked_ticket_userinfo()
        elif x=='0':
            self.exit()
        else:
            print('Choose from the currect option')
            self.options()
        
        
    def showtickets(self):
        print('\n')
        print('Cinema :')
        print(' '.join(self.t))
        for i in self.s:
            print(' '.join(i))
        print('\n')
        
        self.options()
        
    def buyticket(self):
        print('\n')
        x1= input('Row Number : ')
        x2= input('column Number:')
        price=0
        
        
        if int(self.r)*int(self.c)<=60:
            price=10
        if int(self.r)*int(self.c)>=60:
            if int(x1)> int(self.r)/2:
                price = 8
            if int(x1) <=int(self.r)/2:
                price = 10
                
        print('\n')
        print('Price for that seat is '+str(price),'$')
        print('\n')
        print('Would you like to book ?')
        print('Type "yes " for booking "no " for option')
        your=input()
        
        if your == 'yes':
            self.currentincome+=price
            self.userinfo[x1+x2]={}
            print('\n')
            self.userinfo[x1+x2]['Name']=input('Name= ')
            
            self.userinfo[x1+x2]['Gender']=input('Gender=')
            if self.userinfo[x1+x2]['Gender']=='male' or self.userinfo[x1+x2]['Gender']=='female' or self.userinfo[x1+x2]['Gender']=='male' or self.userinfo[x1+x2]['Gender']=='female':
                pass
            else:
                print('Plz Type The Currect Gender')
                self.userinfo[x1+x2]['Gender']= input('Gender =')
                
            self.userinfo[x1+x2]['Age']= input('Age =')
            if self.userinfo[x1+x2]['Age'].isnumeric():
                pass
            else:
                print('plz Type the currect Age')
                self.userinfo[x1+x2]['Age']= input('Age =')
            self.userinfo[x1+x2]['TicketPrice'] = price
            
            self.userinfo[x1+x2]['Phone_no']=input('Phone_no=')
            if self.userinfo[x1+x2]['Phone_no'].isnumeric() and len(self.userinfo[x1+x2]['Phone_no'])==10:
                pass
            else:
                print('Number is invalid.Plz type currect mob no.')
                self.userinfo[x1+x2]['Phone_no']=input('Phone_no =')
                
            print('Congratulations Booked successfully!!!!')
            self.s[int(x1)-1][int(x2)]='B'
            
        if your == 'no':
            print('\n')
            print('Thank you !!!!')
            print('Visit again!!!')
            
        self.options()
        
    def statistics(self):
        
        print('\n')
        print('No of purchased ticketv:',str(len(self.userinfo)))
        print('Percentage : ',str((self.currentincome*100)/self.totalincome)+'%')
        print('Currrent Income : ','$'+str(self.currentincome))
        print('Total Income :','$'+str(self.totalincome))
        print('**** **** **** **** **** **** **** **** **** ****')
        
        self.options()
        
    def show_booked_ticket_userinfo(self):
        print('\n')
        if len(self.userinfo)==0:
            print('Movie Theater completly vacant :')
            self.options()
            
        i=input('Row Number :')
        j=input('column Number :')
        if i+j in self.userinfo:
            print('\n')
            
            
            print('Name :',self.userinfo[i+j]['Name'])
            print('Gender :',self.userinfo[i+j]['Gender'])
            print('Age' ,self.userinfo[i+j]['Age'])
            print('TicketPrice :','$'+str(self.userinfo[i+j]['TicketPrice']))
            print('Phone no= :',self.userinfo[i+j]['Phone no'])
            print('**** **** **** **** **** **** **** **** **** ****')
        else:
            print('\n')
            print(i+j+'Is not bookked yet')
            
        self.options()
        
    def exit(self):
        pass
x= Bookyourmovie()