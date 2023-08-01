def Mealy_Machine(dna1,e):
  m = [
        [0, "A", "T", 1],
        [0, "C", "G", 0],
        [0, "G", "C", 3],
        [0, "T", "A", 2],

        [1, "A", "C", 3],
        [1, "C", "A", 2],
        [1, "G", "G", 0],
        [1, "T", "T", 1],

        [2, "A", "G", 0],
        [2, "C", "T", 1],
        [2, "G", "A", 2],
        [2, "T", "C", 3],

        [3, "A", "A", 2],
        [3, "C", "C", 3],
        [3, "G", "T", 1],
        [3, "T", "G", 0],  # mistake

  ]
  if e==0:
    state = 0
     # given sample input in paper
    dna2 = ""
    for j in dna1:
        for i in m:
            if state == i[0] and j == i[1]:
                state = i[3]
                dna2 += i[2]
                break

    return dna2
  if e==1:
      state = 0
      # given sample input in paper
      dna2 = ""
      for j in dna1:
          for i in m:
              if state == i[0] and j == i[1]:
                  rr=i[2]
                  dna2 += i[2]
                  for q in m:
                      if state == q[0] and rr == q[1]:

                           state = q[3]

                           break
                  break

      return dna2
      # output of given input

