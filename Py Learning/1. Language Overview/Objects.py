class Duck:
    def Sound(self):
        print("Quaaaak!")
    def Walk(self):
        print("Walking like a duck.")
def main():
    donald = Duck()
    donald.Sound()
    donald.Walk()
if __name__ == "__main__": main()