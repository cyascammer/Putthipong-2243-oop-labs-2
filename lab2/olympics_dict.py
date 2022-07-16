'''
Puttthipong Phukhansung
633040224-3
'''

taekwondo_olympics2020_w49k = {
    "Gold": {"Thailand"}
}

taekwondo_olympics2020_w49k.update ({        
    "Silver": {"Spain"},
    "Bronze": {"Israel", "Serbia"},
})

def i():
    for key, value in taekwondo_olympics2020_w49k.items():
        for x in value:
            print(x, "received",key,"medal")

if __name__ == '__main__':
    print("The list of modals in Taekwondo Olympics 2020 women 49 kilograms:")
    i()
    print("The dictionary of medals is", taekwondo_olympics2020_w49k)
