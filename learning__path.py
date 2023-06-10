import time

class learningPath:
    def __init__(self, n = 7):
        self.size = n
        self.front = None
        self.back = None
        self.current_size = 0 # Kosong
        self.data = [None] * n
    
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

# Q = learningPath()
# Q.enqueue("HTML5")
# Q.enqueue("CSS")
# Q.enqueue("Bootstrap")
# Q.enqueue("JavaScript")
# Q.enqueue("Version Control System")
# Q.enqueue("Tailwind")
# Q.enqueue("React")

# print("\nKapasitas\t:", Q.size)
# print("Jumlah item\t:", Q.current_size)
# print("Indeks depan\t:", Q.front)
# print("Indeks belakang\t:", Q.back)
# print("Data\t\t:", Q.data)

# Q.visualisasi()

# isDoneHtml = input("Apakah anda sudah belajar HTML5? [y/n] :")
# if isDoneHtml == "y" or isDoneHtml == "Y":
#     Q.dequeue()
#     Q.visualisasi()
#     isDoneCss = input("Apakah anda sudah belajar CSS? [y/n] :")
#     if isDoneCss == "y" or isDoneHtml == "Y":
#         Q.dequeue()
#         Q.visualisasi()
#     elif isDoneCss == "n" :
#         print("\nAnda belum belajar CSS")
#         Q.visualisasi()
#     else:
#         print("Input tidak valid.")
# elif isDoneHtml == "n" :
#     print("\nAnda belum belajar HTML5")
#     Q.visualisasi()
# else:
    # print("Input tidak valid.")



# isDoneHtml = input("Apakah anda sudah belajar HTML5? [y/n] :")
# if isDoneHtml.lower() == "y":
#     Q.dequeue()
#     Q.visualisasi()
# elif isDoneHtml.lower() == "n":
#     print("Anda belum belajar HTML5.")
#     time.sleep(5)  # Penundaan selama 5 detik
#     isDoneHtml = input("Apakah anda sudah belajar HTML5 sekarang? [y/n] :")
#     Q.visualisasi()
#     if isDoneHtml.lower() == "y":
#         Q.dequeue()
#         Q.visualisasi()
#     elif isDoneHtml.lower() == "n":
#         print("Anda masih belum belajar HTML5.")
#     else:
#         print("Input tidak valid.")
# else:
#     print("Input tidak valid.")