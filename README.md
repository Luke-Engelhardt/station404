# Station 404 🚀
    

A thrilling console-based exploration game where you navigate through an abandoned space station using your scanner to avoid deadly traps.

## About the Game

In Station 404, you find yourself in a mysterious abandoned space station filled with hidden traps. Your mission is to  scan and identify all safe areas while avoiding the deadly traps that could end your mission instantly.
 

### How to Play

- Use your scanner to investigate areas of the space station
- Each safe scan reveals a number indicating how many dangerous areas are adjacent
- Avoid triggering traps - one wrong scan and it's game over!
- Victory is achieved by revealing all safe areas

<img src="https://github.com/user-attachments/assets/2402336b-830a-4012-bb27-bdd60330ac0b" width="400" alt="Station 404 Image">

## Technical Requirements

- Python 3.13.1
- Ubuntu 20.04 LTS or compatible system

## Installation

1. Clone the repository
```bash
git clone https://github.com/Luke-Engelhardt/station404
```

2. Install required packages:
```bash
pip install -r requirements.txt
```
3. Have Fun!
```bash
python3 source/main.py
```

## INSTRUCTIONS  

Welcome to **STATION404**, an abandoned space station filled with deadly traps.  
Your mission: **navigate the wreckage and locate all the traps before it's too late.**  

---

### 🛠 GAME ACTIONS  

#### 1️⃣ SHOW SPACESHIP  
Displays the current **map** of the spaceship, showing explored areas and marked traps.  

#### 2️⃣ SCAN FIELD `(x, y)`  
Scans the selected coordinates for traps:  
   - ❌ **Trap detected** → **GAME OVER**  
   - ⚠️ **Nearby traps** → Shows the number of adjacent traps  
   - ✅ **Safe zone** → The field becomes empty  

#### 3️⃣ MARK FIELD `(x, y)`  
Places an `X` on the selected coordinates to **mark a suspected trap**.  

---

#### ⚡ CAUTION  
One wrong move could seal your fate.  
**Think, scan, and mark wisely to escape STATION404.**  
