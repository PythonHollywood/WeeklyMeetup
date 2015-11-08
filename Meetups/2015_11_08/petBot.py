class Pet:
        def __init__(self):
                self.name = None

                ##############
                # Pet sounds #
                ##############

                self.painCall = 'AAHHHH!!!'
                self.hungerCall = 'me hungry'
                self.eatCall = 'me like sandwich'

                ##############
                # Pet states #
                ##############

                f=open('state.txt','r')
                self.hunger=int(f.readline())
                f.close

                self.mood= int(self.hunger)*.2
                self.dirty = 0

        ###########
        # Actions #
        ###########

        def change(self,stateChange):
                f=open('state.txt','w')
                f.writelines(str(stateChange))
                f.close()

        def spanked(self):
                self.mood -= .25
                print(self.painCall)

        def eat(self):
                eatPet = int(self.hunger)-2
                print(self.eatCall)
                self.change(eatPet)


        def awake(self):
                wake = int(self.hunger)+1
                if self.hunger>0:
                        print(self.hungerCall)
                self.change(wake)
                print(self.hunger)
                print(self.mood)
                self.userAct = raw_input('Do something to your pet!\n')

                if self.userAct == '#spank':
                        self.spanked()
                        print(self.mood)                
                elif self.userAct == '#food':
                        self.eat()

test = Pet()
test.awake()
