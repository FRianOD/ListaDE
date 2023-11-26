class Dado:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
        self.ant = None
    
class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.numeroDeElementos = 0
    
    def estaVazia(self):
        if self.fim == None and self.inicio == None: return True
        else: return False
        
    def tamanho(self):
        return self.numeroDeElementos
        
    def adicionar(self, pos, valor):
        
        if pos >= 0 and pos <= self.numeroDeElementos:
            
            novoDado = Dado(valor)
            
            if self.estaVazia():
                self.inicio = self.fim = novoDado
            
            elif pos == 0 :
                self.inicio.ant = novoDado
                novoDado.prox = self.inicio
                self.inicio = novoDado
                
            elif pos == self.numeroDeElementos:
                self.fim.prox = novoDado
                novoDado.ant = self.fim
                self.fim = novoDado
                
            else:
                temp = self.inicio
                for i in range(pos-1):
                    temp = temp.prox
                novoDado.prox = temp.prox
                temp.prox = novoDado
                novoDado.ant = temp
                novoDado.prox.ant = novoDado
            
            self.numeroDeElementos += 1
            
        else:
            return f"Posição invalida"
                    
    def remover_V(self, valor):
        if self.estaVazia(): return f"Lista Vazia"
        
        lixo = Dado(-1)
        
        if valor == self.inicio.valor and self.numeroDeElementos == 1:
            lixo = self.inicio
            self.inicio = self.fim = None 
            
        if valor == self.inicio.valor:
            
            lixo = self.inicio
            self.inicio = self.inicio.prox
        
        elif valor == self.fim.valor:
            
            lixo = self.fim
            self.fim = self.fim.ant
            
        else:
            temp = self.inicio
            
            while temp.prox != None and valor != temp.prox.valor:
                    temp = temp.prox
                    
            if temp.prox is not None:
                lixo = temp.prox
                temp.prox = temp.prox.prox
                temp.prox.ant = temp
            
        self.numeroDeElementos -= 1
        return lixo.valor
    
    def remover_P(self, pos):
    
        if self.estaVazia(): return f"Lista Vazia"
        
        lixo = Dado(-1)
        
        if pos == 0 and self.numeroDeElementos == 1:
            lixo = self.inicio
            self.inicio = self.fim = None 
            
        elif pos == 0:
            lixo = self.inicio
            self.inicio = self.inicio.prox
        
        elif pos == self.numeroDeElementos - 1:
            lixo = self.fim
            self.fim = self.fim.ant
            
        else:
            temp = self.inicio
            
            for i in range(pos-1) :
                    temp = temp.prox
            
            if temp.prox != None:
                lixo = temp.prox
                temp.prox = temp.prox.prox
                temp.prox.ant = temp
        
        self.numeroDeElementos -= 1
        return lixo.valor
    
    def buscar_V(self, valor):
        if self.estaVazia(): return f"Lista Vazia"
        
        dado = Dado(-1)
        posicao = -1
        if valor == self.inicio.valor:
            dado = self.inicio
            posicao = 0
            
        elif valor == self.fim.valor:
            dado = self.fim
            posicao = self.numeroDeElementos - 1
        
        else:
            temp = self.inicio
            posicao = 1
            while temp.prox != None and valor != temp.prox.valor:
                    temp = temp.prox
                    posicao +=1
                    
            if temp.prox is not None:
                dado = temp.prox
                
            else:
                posicao = -1
            
        if dado == -1 or posicao == -1:
            return f"Valor não encontrado"
        else:
            return f"Valor {dado.valor} encontrado na posição {posicao} da lista"
    
    def buscar_P(self, pos):
        if self.estaVazia(): return "Lista Vazia"
        
        dado = Dado(-1)
        if pos == 0:
            dado = self.inicio
        elif pos == self.numeroDeElementos-1:
            dado = self.fim
        else:
            temp = self.inicio
            
            for i in range(pos):
                    temp = temp.prox
            
            if temp.prox != None:
                dado = temp.prox
        
        return dado.valor
            
    def imprimirLista(self):
        if self.estaVazia(): return "Lista Vazia"
        
        temp = self.inicio
        print("[", end="")
        while temp.prox != None:
            print(f"{temp.valor},", end="")
            temp = temp.prox
        else:
            print(f"{temp.valor}]")
    
    def imprimirReversa(self):
        if self.estaVazia(): return "Lista Vazia"
        
        temp = self.fim
        print("[", end="")
        while temp.ant != None:
            print(f"{temp.valor},", end="")
            temp = temp.ant
        else:
            print(f"{temp.valor}]")
        