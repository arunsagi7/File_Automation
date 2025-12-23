import os
import streamlit as st

def filecreater(path):
    extensions = []
    files = os.listdir(path)

    for i in files:
        if os.path.isfile(os.path.join(path, i)):
            ext = os.path.splitext(i)[1][1:]
            if ext:
                folder_path = os.path.join(path, ext)
                if folder_path not in extensions:
                    extensions.append(folder_path)

    for folder in extensions:
        os.makedirs(folder, exist_ok=True)

        for file in files:
            if os.path.isfile(os.path.join(path, file)):
                if os.path.splitext(file)[1][1:] == os.path.basename(folder):
                    os.rename(
                        os.path.join(path, file),
                        os.path.join(folder, file)
                    )

    return [os.path.basename(f) for f in extensions]


# -------- Streamlit UI -------- #
st.set_page_config(page_title="File Organizer", layout="centered")

st.title("📂 File Organizer by Extension")
st.write("Enter a folder path to organize files into subfolders based on extensions.")

path = st.text_input(
    "Folder Path",
    placeholder=r"C:\Users\arunk\OneDrive\Desktop\Automation_File"
)

if st.button("Organize Files"):
    if path and os.path.exists(path):
        try:
            folders = filecreater(path)
            st.success("Files organized successfully! ✅")

            if folders:
                st.write("Created folders:")
                st.write(", ".join(folders))
            else:
                st.info("No files with extensions found.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid folder path.")
