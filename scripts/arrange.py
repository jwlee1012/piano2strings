from music21 import converter, stream, instrument, note

melody = converter.parse('../data/melody.mid')
melody_part = melody.parts[0].flat.notes

chord_map = {
    'C': ['C', 'E', 'G'],
    'D': ['D', 'F#', 'A'],
    'E': ['E', 'G#', 'B'],
    'F': ['F', 'A', 'C'],
    'G': ['G', 'B', 'D'],
    'A': ['A', 'C#', 'E'],
    'B': ['B', 'D#', 'F#']
}

violin1 = stream.Part()
viola = stream.Part()
cello = stream.Part()
violin1.insert(0, instrument.Violin())
viola.insert(0, instrument.Viola())
cello.insert(0, instrument.Violoncello())

for n in melody_part.notes:
    if isinstance(n, note.Note):
        root = n.name[0]
        if root in chord_map:
            triad = chord_map[root]
            violin1.append(note.Note(triad[0], quarterLength=n.quarterLength))
            viola.append(note.Note(triad[1], quarterLength=n.quarterLength))
            cello.append(note.Note(triad[2], quarterLength=n.quarterLength))

score = stream.Score()
score.insert(0, violin1)
score.insert(0, viola)
score.insert(0, cello)

score.write('midi', fp='../output/orchestra.mid')