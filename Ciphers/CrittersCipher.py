import binascii
import random

import numpy as np
from matplotlib import pyplot as plt


class CrittersCipher:
    
    def __init__(self):
        self.binstrLength = None
        self.blockDimensions = [100,100]
        n = self.blockDimensions[0]
        initialGrid = np.random.choice(2, n**2, p=[.5, .5]).reshape(n, n)
        self.img = plt.imshow(initialGrid, cmap='gray', interpolation='nearest')

    def animate(self, plainblocks):
        self.img.set_data(plainblocks[0])
        plt.pause(0.1)

    def encrypt(self, plaintext, cycles):
        plainblocks = self.convertToBitsThenBlocks(plaintext)
        print(plainblocks)
        flicker = 0
        for i in range(cycles):
            plainblocks = self.runOneEncryptionCycle(plainblocks)
            print(plainblocks)
            flicker += 1
            if flicker % 2 == 0:
                self.animate(plainblocks)
        ciphertext = self.isolateResult(plainblocks)
        return ciphertext

    def isolateResult(self, plainblocks):
        binstr = ""
        count = 0
        for i in plainblocks:
            for x in i:
                for y in x:
                    if count >= self.binstrLength:
                        break
                    else:
                        binstr += str(y)
                    count += 1
        binary_chunks = [binstr[i:i + 8] for i in range(0, len(binstr), 8)]
        ascii_characters = ''.join([chr(int(chunk, 2)) for chunk in binary_chunks])
        return ascii_characters

    def convertToBitsThenBlocks(self, plaintext):
        hex_str = binascii.hexlify(plaintext.encode())
        bin_str = bin(int(hex_str, 16))[2:].zfill(8 * ((len(hex_str) + 1) // 2))
        self.binstrLength = len(bin_str)
        result = []
        count = 0
        while count < len(bin_str):
            newBlock = []
            for x in range(self.blockDimensions[0]):
                newRow = []
                for y in range(self.blockDimensions[1]):
                    if count >= len(bin_str):
                        r = random.random()
                        if r < .2:
                            newRow.append(1)
                        else:
                            newRow.append(0)
                    else:
                        newRow.append(int(bin_str[count]))
                        count += 1
                newBlock.append(newRow)
            result.append(newBlock)
        print("original", bin_str)
        return result

    def runOneEncryptionCycle(self, plainblocks):
        for b in range(len(plainblocks)):
            for x in range(0, len(plainblocks[b]), 2):
                for y in range(0, len(plainblocks[b][x]), 2):
                    count = 0
                    if plainblocks[b][x][y] == 1:
                        count += 1
                    if plainblocks[b][x+1][y] == 1:
                        count += 1
                    if plainblocks[b][x][y+1] == 1:
                        count += 1
                    if plainblocks[b][x+1][y+1] == 1:
                        count += 1
                    if count == 2:
                        continue
                    elif count == 0 or count == 1 or count == 3 or count == 4:
                        plainblocks[b][x][y] = self.flip(plainblocks[b][x][y])
                        plainblocks[b][x + 1][y] = self.flip(plainblocks[b][x + 1][y])
                        plainblocks[b][x][y + 1] = self.flip(plainblocks[b][x][y + 1])
                        plainblocks[b][x + 1][y + 1] = self.flip(plainblocks[b][x+1][y+1])
                    if count == 3:
                        temp = plainblocks[b][x][y]
                        plainblocks[b][x][y] = plainblocks[b][x + 1][y + 1]
                        plainblocks[b][x + 1][y + 1] = temp

                        temp = plainblocks[b][x + 1][y]
                        plainblocks[b][x + 1][y] = plainblocks[b][x][y + 1]
                        plainblocks[b][x][y + 1] = temp
        return plainblocks



    def flip(self, val):
        if val == 1:
            return 0
        return 1




critters = CrittersCipher()
ciphertext = critters.encrypt("asdfkjlsa", 10)
print("ENCRYPTION RESULT", ciphertext)
plaintext = critters.encrypt(ciphertext, 10)
print("DECRYPTION RESULT", plaintext)
