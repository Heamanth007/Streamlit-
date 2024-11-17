import streamlit as st
import random as r


def computer_guessing():
    if 'num1' not in st.session_state:
        st.session_state.num1 = 0
    if 'num2' not in st.session_state:
        st.session_state.num2 = 100

    st.title("Computer Guessing Mode")
    
    num1 = st.number_input("Enter the Starting Range", min_value=0, max_value=100, value=st.session_state.num1)
    num2 = st.number_input("Enter the Ending Range", min_value=0, max_value=100, value=st.session_state.num2)

    if st.button("START"):
        if num1 > num2:
            st.write("Starting Range is higher than Ending Range. Please enter a valid range.")
        else:
            st.session_state.num1 = num1
            st.session_state.num2 = num2
            guess = r.randint(num1, num2)
            if "guess" not in st.session_state:
                st.session_state.guess=guess
            st.subheader(f"Computer guess: {guess}")
    feedback=st.radio("How is the machine guess ?",("CORRECT","Too High","Too Low"))
    if st.button("SUBMIT"):
        if feedback=="CORRECT":
            st.write("Correct")
            st.balloons()
        elif feedback=="Too High":
            st.session_state.num2 = st.session_state.guess - 1
            st.session_state.guess = (st.session_state.num1 + st.session_state.num2) // 2
            st.write(f"The machine's new guess is {st.session_state.guess}")
            
        elif feedback=="Too Low":
            st.session_state.num1 = st.session_state.guess + 1
            st.session_state.guess = (st.session_state.num1 + st.session_state.num2) // 2
            st.write(f"The machine's new guess is {st.session_state.guess}")
        
        
    


def user_guessing():
    st.title("User Guessing Mode")
        
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = r.randint(0, 100)

    guess = st.number_input("Guess the number (0 to 100)", min_value=0, max_value=100)

    if st.button("Submit Guess"):
        if guess < st.session_state.secret_number:
            st.write("Your guess is too low! Try again.")
        elif guess > st.session_state.secret_number:
            st.write("Your guess is too high! Try again.")
        else:
            st.write("Congratulations! You guessed the correct number!")
            st.balloons()
    if st.button("Reset Game"):
         del st.session_state.secret_number 

def Portfolio():
    st.title("Portfolio")
    st.subheader("Name: Heamanthraj.S")
    st.subheader("College: KGiSl Institute of Technology")
    st.subheader("Branch: B.Tech IT")
    st.subheader("School: Ramco Vidya Mandir Snior Secondary School")
    st.subheader("Native: Ariyalur")

    


with st.sidebar:
    a = st.radio("Choice", ("Portfolio","Computer Guessing", "User Guessing"))


if a == "Computer Guessing":
    computer_guessing()
elif a == "User Guessing":
    user_guessing()
elif a=="Portfolio":
    Portfolio()
