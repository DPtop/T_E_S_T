class Public_Protected_Private:
    def __init__(self, a_public:str='PUBlic', a_protected:str='proTECted', a_private:str='privATE'):
        self.a_public = a_public            # открытый
        self._a_protected = a_protected     # доступный и наследнику
        self.__a_private = a_private        # закрытый вне класса

    def show(self):
        print(self.a_public + '\n' + self._a_protected + '\n' + self.__a_private)


class Check_atributes(Public_Protected_Private):
    def check_show(self):
        self.show()
        print('**',
              self.a_public,        # покажет
              self._a_protected)    # покажет
              #self.__a_private)    # не покажет => AttributeError: 'Check_atributes' object has no attribute '_Check_atributes__a_private'


Check_atributes().check_show()

