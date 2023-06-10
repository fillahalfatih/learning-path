class learningPath:
    def __init__(self, n = 7):
        self.size = n
        self.front = None
        self.back = None
        self.current_size = 0 # Kosong
        self.data = [None] * n
    
    def peek(self):
        if self.current_size > 0:
            return self.data[self.front]
        else:
            return None

    def is_empty(self):
        return self.current_size == 0
    
    # Memasukan item ke frontEnd
    def enqueue(self, x):
        print("[Enqueue :", x, end="], ")
        if self.current_size < self.size :
            if self.current_size == 0 :
                self.front = self.back = 0
            else :
                self.back = self.back + 1
                if self.back == self.size :
                    self.back = 0
            self.data[self.back] = x
            self.current_size = self.current_size + 1 
        else: # penuh
            print(x, "Gagal melakukan Enqueue")

    def dequeue(self):
        if self.current_size > 0: #ada isinya
            hasil = self.data[self.front]
            self.front = self.front + 1
            if self.front ==self.size:
                self.front = 0
            self.current_size = self.current_size - 1
        else : # kosong
            print("Dequeue gagal dilakukan")
            hasil = None
        return hasil

    def visualisasi(self):
        print()
        print("=" * 82)
        # yang kosong
        for i in range(self.size - self.current_size):
            print("%0s | " % (" "), end="", sep="")
        # yang isi
        for i in range(self.current_size):
            print("%0s | " % (self.data[self.back - i]), end="", sep="")
        print()
        print("=" * 82)
        print()