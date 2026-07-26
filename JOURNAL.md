---
title: "GridAspect"
author: "TheAbsoluteMin"
description: "Pen Plotter."
created_at: "2026-07-22"
---

# GridAspect Development Log

## Log 1: July 22, 2026 - Initial CAD Design - 5.5 hours
Timelapse <a href="https://lapse.hackclub.com/timelapse/-1ezrf_tdW6T">link</a>.

### Inspiration:
I have always played with the idea of a pen plotter, and I have found pictures of them on the internet to be amazing. Instead of using an expensive printer, a pen can create beautiful art cheaply. A few months earlier, I attempted to create a pocket pen plotter on wheels because I did not like the bulky, huge form factor of two axis plotters and linear rails. However, the tiny pen plotter quickly became complex as it was extremely difficult to fit all the necessary parts in a small form factor. I left that project for some time until now when I obtained temporary access to a laser cutter, 3D printer, and GoPiGo3 kit! Thus, I decided to embrace the slightly big form factor, and make a small pen plotter with my given materials without relying on traditional stepper motors and linear rails!

Usually, when I first begin a project, I create schematics and a PCB. However, I wanted to prototype the mechanical design of a pen plotter actuated by hobby DC motors with magnetic encoders and wooden gears and rails. Thus, I began to learn how to create the CAD parts that I would 3D print and laser cut.

<img width="2534" height="1197" alt="image" src="https://github.com/user-attachments/assets/03b0833d-8284-4910-8af8-a2c3aa373b57" />

One key difficulty was learning a new CAD software. I was accustomed to Autodesk Fusion for some time, but I wanted to learn how to use Onshape. After some time playing around, I figured out how to use it.

<img width="2535" height="1202" alt="image" src="https://github.com/user-attachments/assets/52240737-1098-4324-830a-9ba218ab0fe6" />


### Future work:
I will continue to work on the CAD design next time!

---

## Log 2: July 23, 2026 - CAD Design Continued - 2.7 hours
Timelapse <a href="https://lapse.hackclub.com/timelapse/8BHEPhD5V7K1">link</a>.

Today, I continued to work on my pen plotter design, and I had to create specific parts with connectors so that each 3D printed part and laser-cut wood part would snap together. It quickly became repetitive to measure and check the dimensions of each component and connection. I had to be careful since the gears had to roll smoothly with the gear racks.

<img width="2528" height="1192" alt="image" src="https://github.com/user-attachments/assets/dff5777a-633a-4d19-ba16-c26e076e0874" />

I also needed to keep in mind the weight of each part. The top rail had to be balanced because each side would carry heavy parts, including a DC motor, micro servo, and pen holder with pen.

<img width="2546" height="1200" alt="image" src="https://github.com/user-attachments/assets/5e327530-16ec-433d-b21b-0af2c5c053b7" />

With some time, I created a rough design of my pen plotter.

<img width="1405" height="1025" alt="image" src="https://github.com/user-attachments/assets/30dbf55b-5611-4c20-a337-d83f7d049489" />

However, I realized that I needed to adapt the gears to fit the motors, so I made some adjustments to the gears.

<img width="2542" height="1201" alt="image" src="https://github.com/user-attachments/assets/497e973c-2a47-4b40-bd1c-3e2419a171bd" />

Finally, I confirmed that all the pieces would fit together.

<img width="1499" height="979" alt="image" src="https://github.com/user-attachments/assets/d9f1da67-d6ec-4f22-8ca7-b15459e6f954" />

### Future work:
I will attempt to print the pieces and make adjustments to the parts as needed.

---

## Log 3: July 24, 2026 - Initial Prototype Assembly - 1 hour
Timelapse <a href="https://lapse.hackclub.com/timelapse/JKGEtxAWUYZX">link</a>.

Having access to a wood laser cutter was an incredible advantage in the design process as the laser cutter cuts incredibly fast, meaning I could prototype faster than before.

https://docs.google.com/videos/d/1d2uOvWI_O6an11SgNBg7lT3CKMpHWUqGn6D0XDg0AWQ/play?usp=sharing 

<img width="2535" height="1231" alt="image" src="https://github.com/user-attachments/assets/e9292444-2971-4ea8-bcab-c6696eddb971" />

After printing and assembling the parts to see how they fit with each other, I found out that the gears, rails, and structural base mostly worked!

<img width="4000" height="3000" alt="20260724_234620" src="https://github.com/user-attachments/assets/4cb41197-ee6f-452c-a7f0-9f3698a07d95" />
<img width="4000" height="3000" alt="20260724_234553" src="https://github.com/user-attachments/assets/2b608280-61b0-40f7-88e4-ebbaa9747548" />
<img width="4000" height="3000" alt="20260724_234541" src="https://github.com/user-attachments/assets/4db08b4e-d66e-4add-82e0-4585280e29a0" />
<img width="3000" height="4000" alt="20260724_234509" src="https://github.com/user-attachments/assets/d6bef2de-e9fc-4edd-a849-5fdee3473387" />

However, there were some slight difficulty in the gear connections with the motors, so I decided to clean up the CAD parts a bit, and I added some color to the design! Also, I decided to include a Raspberry Pi Camera Model 3 and a Raspberry Pi 4, so I could possibly allow the pen plotter to take pictures and draw in real time!

<img width="1474" height="979" alt="Screenshot 2026-07-24 131920" src="https://github.com/user-attachments/assets/02e672c1-7ea3-4ce2-a68f-865883ff15ff" />

### Future work:
I will attempt to reprint the flawed parts and reassemble everything again, so I can test out some code to see how the motors and gears interact with the gear racks.

---
