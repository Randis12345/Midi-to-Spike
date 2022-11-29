import mido

# track for spike to play
TRACK_NUM = 1

# create mido object from midi file
mid = mido.MidiFile(r"Super Mario 64 - Medley.mid")

# list of all note messages from the midifile
mess = [x.dict() for x in mid.tracks[TRACK_NUM] if x.dict()["type"] in ["note_off","note_on"]]

instruct = []

#loops through each note messages and converts it into instructions for spike
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

# caps instructions at 220 and prints them
if len(instruct) > 220:
    print(instruct[:220])
else:
    print(instruct)     