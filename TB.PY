import sys

def main():
    while True:
        print("\n🔹 اختر خيارًا:")
        print("1️⃣ طباعة 'Hello, World!'")
        print("2️⃣ إغلاق البرنامج")
        
        choice = input("👉 أدخل رقم الخيار: ")

        if choice == "1":
            print("\n🌍 Hello, World!\n")
        elif choice == "2":
            print("\n👋 يتم إغلاق البرنامج... 🚀\n")
            sys.exit(0)
        else:
            print("\n⚠️ خيار غير صالح! حاول مرة أخرى.")

if __name__ == "__main__":
    main()
