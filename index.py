import streamlit as st

# Initialize session state for the library
if 'library' not in st.session_state:
    st.session_state.library = []

def add_book():
    with st.form("Add Book"):
        title = st.text_input("Title")
        author = st.text_input("Author")
        year = st.number_input("Publication Year", min_value=0, max_value=3000, step=1)
        genre = st.text_input("Genre")
        read = st.checkbox("Read?")
        submitted = st.form_submit_button("Add")
        if submitted:
            book = {
                'title': title,
                'author': author,
                'year': year,
                'genre': genre,
                'read': read
            }
            st.session_state.library.append(book)
            st.success("Book added successfully.")

def remove_book():
    titles = [book['title'] for book in st.session_state.library]
    if titles:
        to_remove = st.selectbox("Select book to remove", titles)
        if st.button("Remove Book"):
            st.session_state.library = [book for book in st.session_state.library if book['title'] != to_remove]
            st.success("Book removed successfully.")
    else:
        st.info("No books to remove.")

def search_books():
    query = st.text_input("Search by Title or Author")
    if query:
        results = [book for book in st.session_state.library if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
        if results:
            for book in results:
                print_book(book)
        else:
            st.warning("No matching books found.")

def display_books():
    if not st.session_state.library:
        st.info("Library is empty.")
    else:
        for book in st.session_state.library:
            print_book(book)

def print_book(book):
    st.write(f"**Title:** {book['title']}")
    st.write(f"**Author:** {book['author']}")
    st.write(f"**Year:** {book['year']}")
    st.write(f"**Genre:** {book['genre']}")
    st.write(f"**Read:** {'Yes' if book['read'] else 'No'}")
    st.markdown("---")

def display_statistics():
    total = len(st.session_state.library)
    read = len([book for book in st.session_state.library if book['read']])
    percent_read = (read / total * 100) if total else 0
    st.write(f"**Total books:** {total}")
    st.write(f"**Books read:** {read} ({percent_read:.2f}%)")

# Streamlit App
st.title("📚 Personal Library Manager")

option = st.sidebar.selectbox(
    "Choose an action",
    ("Add Book", "Remove Book", "Search Books", "Display All Books", "Statistics")
)

if option == "Add Book":
    add_book()
elif option == "Remove Book":
    remove_book()
elif option == "Search Books":
    search_books()
elif option == "Display All Books":
    display_books()
elif option == "Statistics":
    display_statistics()
