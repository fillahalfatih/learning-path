import os
import time
from learning__path import learningPath

if __name__ == "__main__":
    operation_system = os.name
    if operation_system == "posix":
        os.system("clear")
    elif operation_system == "nt":
        os.system("cls")

    print("==========================================")
    print("||          SELAMAT DATANG DI           ||")
    print("||   PROGRAM SEDERHANA LEARNING PATH    ||")
    print("||           ~WEB DEVELOPMENT           ||")
    print("==========================================")

    while True:
        if operation_system == "posix":
            os.system("clear")
        elif operation_system == "nt":
            os.system("cls")

        print("==========================================")
        print("||          SELAMAT DATANG DI           ||")
        print("||   PROGRAM SEDERHANA LEARNING PATH    ||")
        print("||           ~WEB DEVELOPMENT           ||")
        print("==========================================")

        print("\n1. Belajar Front-End")
        print("2. Belajar Back-End")
        print("3. Belajar Full-Stack\n")

        user_option = input("Mau belajar apa hari ini? : ")
        print()

        if user_option == "1":
            front_end = learningPath()
            front_end.enqueue("HTML5")
            front_end.enqueue("CSS")
            front_end.enqueue("Bootstrap")
            front_end.enqueue("JavaScript")
            front_end.enqueue("Version Control System")
            front_end.enqueue("Tailwind")
            front_end.enqueue("React")
            front_end.visualisasi()

            while not front_end.is_empty():
                current_topic = front_end.peek()
                learned = input("Apakah Anda sudah mempelajari {}? [y/n]: ".format(current_topic))

                if learned.lower() == "n":
                    print("\n> Anda harus belajar {} terlebih dahulu\n".format(current_topic))
                    time.sleep(2.5)
                elif learned.lower() == "y":
                    front_end.dequeue()
                    front_end.visualisasi()
                else:
                    print("\nPilihan tidak ada di opsi. Silakan masukkan 'y' atau 'n'.\n")

            print("> Selamat, Anda sudah menjadi seorang front-end developer!\n")

        elif user_option == "2":
            back_end = learningPath()
            back_end.enqueue("Python")
            back_end.enqueue("Flask")
            back_end.enqueue("Django")
            back_end.enqueue("Database")
            back_end.enqueue("RESTful API")
            back_end.enqueue("Authentication")
            back_end.enqueue("Deployment")
            back_end.visualisasi()

            while not back_end.is_empty():
                current_topic = back_end.peek()
                learned = input("Apakah Anda sudah mempelajari {}? [y/n]: ".format(current_topic))

                if learned.lower() == "n":
                    print("\n> Anda harus belajar {} terlebih dahulu\n".format(current_topic))
                    time.sleep(2.5)
                elif learned.lower() == "y":
                    back_end.dequeue()
                    back_end.visualisasi()
                else:
                    print("\nPilihan tidak ada di opsi. Silakan masukkan 'y' atau 'n'.\n")

            print("> Selamat, Anda sudah menjadi seorang back-end developer!\n")

        elif user_option == "3":
            ask = input("[y/n] : ")
            print("Apakah Anda sudah menguasai front-end web development?", ask)

            if ask.lower == "n" :
                print("Anda harus menguasai front-end web development terlebih dahulu.")

        else:
            print("\nTidak ada di opsi")

        is_done = input("Apakah selesai [y/n]? ")
        if is_done.lower() == "y":
            break

    print("\n~ Program berakhir, Terima kasih\n")
