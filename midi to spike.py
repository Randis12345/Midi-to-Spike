import mido,scamp

TRACK_NUM = 8

mid = mido.MidiFile(r"Super Mario 64 - Medley.mid")

mess = [x.dict() for x in mid.tracks[1] if x.dict()["type"] in ["note_off","note_on"]]

instruct = []#[[x["note"],x["time"]] for x in mess if x["type"] == "note_on"]


for xi,x in enumerate(mess):
    if x["type"] == "note_on":
        time_sum = 0
        if not xi == len(mess)-1:
            for y in mess[xi+1:]:
                time_sum+=y["time"]
                if y ["type"] == "note_on":
                    break
            if time_sum == 0: time_sum = 1
            instruct.append([x["note"],time_sum])
        else:
            instruct.append([x["note"],1])

        
for x in instruct: print(x)

sess = scamp.Session()
sess.tempo = 150000
piano = sess.new_part("paino")

for x in instruct: piano.play_note(x[0],1,x[1])