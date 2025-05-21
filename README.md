# Resolve Script Linker

This Python script simplifies the process of creating a symbolic link between your custom script directory and **DaVinci Resolve’s default Fusion script folder**. This is incredibly useful for developers who want to work on their scripts from a version-controlled folder (like a GitHub clone) while still making them accessible within Resolve without manual copying.

---

## 📦 What It Does

When run with administrator privileges, this script will:

- Detect your operating system.
- Locate the default DaVinci Resolve Fusion `Scripts/Comp` folder.
- Create a **symbolic link** between the directory where the script is located and the Fusion script folder.

This allows DaVinci Resolve to directly access your scripts from your custom folder (e.g., a GitHub clone).

---

## ⚠️ Prerequisites

- Python 3.x installed.
- You **must run the script as administrator**.

---

## 🛠️ Instructions

### 1. Clone this Repository

```bash
git clone https://github.com/yibebiz/resolve-script-linker.git

```
### 2. Copy the Script
Copy the `symbolic_link_setup.py` file into your desired project folder. For example:
```
project/
└── demo1/
    └── symbolic_link_setup.py
```
###  3. Run the Script
Open a terminal or command prompt as Administrator, then navigate to the `demo1` folder and run:

```bash

python symbolic_link_setup.py

```

###  ✅ Expected Outcome
This will create a symbolic link from:

```bash
<your local folder>/demo1
```
to:

```bash
<DaVinci default Fusion script folder>/demo1
```
Now, your scripts located in `demo1` will appear automatically in DaVinci Resolve Workspace Scripts!

### 📝 License
This project is licensed under the MIT License.
Let me know if you'd like it tailored with your actual GitHub username or project-specific details.



