
# Project RamJet

## Table of Contents
1. [Introduction](#introduction)
2. [Vision](#vision)
3. [Functional Requirements](#functional-requirements)
4. [Quality Requirements](#quality-requirements)

---

## Chapter 1: Introduction

**Documentation Purpose**: This document is intended for the target audience belonging to the group [Task teachers]:
- Kylmäniemi Ilkka
- Tauriainen Juha

**Project Team**: Task Team [Group 6], comprising:
- Nadim Bhuiyan
- Tanvir Nibir
- Kiavash Montazeri
- Timur Sindirinschi

This document and its contents have been prepared for **Project RamJet**.

**Contents:**
1. **Introduction Page**
   - Target audience
   - Project team
   - Project name
2. **Vision Page**
   - Names for in-game entities
   - Functionality and relationship between entities
   - Description of the purpose
3. **Functional Requirements**
4. **Quality Requirements**

---

## Chapter 2: Vision

In **Project RamJet**, the game is led by the protagonist, referred to as [The Traveler]. **Traveling** is the main activity, allowing the player to explore **The World** using different types of aircraft, known as [Frigates].

**Game Entities:**
- **The World**: A vast space filled with cross-winds, called **Zephyrs**, guided by meteorological conditions defined by **The Elements**. The space is further influenced by a ceiling entity called **The Ether**, which mimics atmospheric pressure.
- **Frigates**: Aircraft used by **The Traveler**. Frigates vary in size, shape, and travel capability, with more powerful versions available for purchase using in-game currency, **Concords**.
- **Concords**: Currency that can be earned through exploration and completing quests. Concords are used to buy equipment, acquire new Frigates, and unlock restricted areas.
- **Sedentars**: Non-player characters who may assist or challenge **The Traveler**. Aligning with **The Sedentary Fate** leads to debuffs or game over.

The ultimate purpose of the game is left for the player to unravel as they progress through the storyline.

---

## Chapter 3: Functional Requirements

- **The Traveler**: Players can travel to various locations, provided their **Frigate's** flight range meets the required distance. Fuel limitations are not a factor.
- **Aircraft Selection**: Players start with a choice between two Frigates, with additional models available for purchase using **Concords**.
- **Quests and Open-world Exploration**: The Traveler can follow the main storyline or explore the world freely, with quests assigned by **Sedentars**.
- **Earning Concords**: Currency is earned by:
  - Traveling to new locations
  - Covering significant distances
  - Completing quests
- **Meteorological Challenges**: Locations present various environmental conditions called **The Elements**, which may require specific **Frigates** or accessories:
  - **Zephyrs**: Cross-winds affecting travel routes.
  - **The Ether**: Atmospheric pressure impacting travel.
  - **Elements**: Weather conditions, such as temperature, that may restrict access without proper equipment.

---

## Chapter 4: Quality Requirements

- **Feedback**: Actions must provide instant feedback to the player.
- **Performance**:
  - Database fetching must not exceed 2 seconds.
  - Code must be optimized for minimal lines and high speed.
  - Waiting times should be kept low and unnoticeable.
- **User Experience**:
  - The storyline must be engaging and prevent boredom.

---
