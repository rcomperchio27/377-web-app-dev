count = 1
for i in range(670442572801):
    if count % 11 == 0 and count % 12 == 0 and count % 13 == 0 and count % 14 == 0 and count % 15 == 0 and count % 16 == 0 and count % 17 == 0 and count % 18 == 0 and count % 19 == 0 and count % 20 == 0:
        final = count
        break
    count += 1
print('done')
print(final)
print(11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20)