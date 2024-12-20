from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 174
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=14)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	T2_in = S.Task('T2_in', length=1, delay_cost=1)
	S += T2_in >= 1
	T2_in += MM_in[0]

	T2_mem0 = S.Task('T2_mem0', length=1, delay_cost=1)
	S += T2_mem0 >= 1
	T2_mem0 += MAIN_MEM_r[0]

	T2_mem1 = S.Task('T2_mem1', length=1, delay_cost=1)
	S += T2_mem1 >= 1
	T2_mem1 += MAIN_MEM_r[1]

	T2 = S.Task('T2', length=14, delay_cost=1)
	S += T2 >= 2
	T2 += MM[0]

	T4_in = S.Task('T4_in', length=1, delay_cost=1)
	S += T4_in >= 2
	T4_in += MM_in[0]

	T4_mem0 = S.Task('T4_mem0', length=1, delay_cost=1)
	S += T4_mem0 >= 2
	T4_mem0 += MAIN_MEM_r[0]

	T4_mem1 = S.Task('T4_mem1', length=1, delay_cost=1)
	S += T4_mem1 >= 2
	T4_mem1 += MAIN_MEM_r[1]

	T3_in = S.Task('T3_in', length=1, delay_cost=1)
	S += T3_in >= 3
	T3_in += MM_in[0]

	T3_mem0 = S.Task('T3_mem0', length=1, delay_cost=1)
	S += T3_mem0 >= 3
	T3_mem0 += MAIN_MEM_r[0]

	T3_mem1 = S.Task('T3_mem1', length=1, delay_cost=1)
	S += T3_mem1 >= 3
	T3_mem1 += MAIN_MEM_r[1]

	T4 = S.Task('T4', length=14, delay_cost=1)
	S += T4 >= 3
	T4 += MM[0]

	T3 = S.Task('T3', length=14, delay_cost=1)
	S += T3 >= 4
	T3 += MM[0]

	T5_in = S.Task('T5_in', length=1, delay_cost=1)
	S += T5_in >= 4
	T5_in += MM_in[0]

	T5_mem0 = S.Task('T5_mem0', length=1, delay_cost=1)
	S += T5_mem0 >= 4
	T5_mem0 += MAIN_MEM_r[0]

	T5_mem1 = S.Task('T5_mem1', length=1, delay_cost=1)
	S += T5_mem1 >= 4
	T5_mem1 += MAIN_MEM_r[1]

	T5 = S.Task('T5', length=14, delay_cost=1)
	S += T5 >= 5
	T5 += MM[0]

	T7_in = S.Task('T7_in', length=1, delay_cost=1)
	S += T7_in >= 5
	T7_in += MM_in[0]

	T7_mem0 = S.Task('T7_mem0', length=1, delay_cost=1)
	S += T7_mem0 >= 5
	T7_mem0 += MAIN_MEM_r[0]

	T7_mem1 = S.Task('T7_mem1', length=1, delay_cost=1)
	S += T7_mem1 >= 5
	T7_mem1 += MAIN_MEM_r[1]

	T6_in = S.Task('T6_in', length=1, delay_cost=1)
	S += T6_in >= 6
	T6_in += MM_in[0]

	T6_mem0 = S.Task('T6_mem0', length=1, delay_cost=1)
	S += T6_mem0 >= 6
	T6_mem0 += MAIN_MEM_r[0]

	T6_mem1 = S.Task('T6_mem1', length=1, delay_cost=1)
	S += T6_mem1 >= 6
	T6_mem1 += MAIN_MEM_r[1]

	T7 = S.Task('T7', length=14, delay_cost=1)
	S += T7 >= 6
	T7 += MM[0]

	T6 = S.Task('T6', length=14, delay_cost=1)
	S += T6 >= 7
	T6 += MM[0]

	T9_in = S.Task('T9_in', length=1, delay_cost=1)
	S += T9_in >= 14
	T9_in += MM_in[0]

	T9_mem0 = S.Task('T9_mem0', length=1, delay_cost=1)
	S += T9_mem0 >= 14
	T9_mem0 += MAIN_MEM_r[0]

	T9_mem1 = S.Task('T9_mem1', length=1, delay_cost=1)
	S += T9_mem1 >= 14
	T9_mem1 += MM_MEM[1]

	T9 = S.Task('T9', length=14, delay_cost=1)
	S += T9 >= 15
	T9 += MM[0]

	T21_in = S.Task('T21_in', length=1, delay_cost=1)
	S += T21_in >= 31
	T21_in += MAS_in[1]

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 31
	T21_mem0 += MM_MEM[0]

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 31
	T21_mem1 += MM_MEM[1]

	T23_in = S.Task('T23_in', length=1, delay_cost=1)
	S += T23_in >= 31
	T23_in += MM_in[0]

	T23_mem0 = S.Task('T23_mem0', length=1, delay_cost=1)
	S += T23_mem0 >= 31
	T23_mem0 += MAS_MEM[0]

	T23_mem1 = S.Task('T23_mem1', length=1, delay_cost=1)
	S += T23_mem1 >= 31
	T23_mem1 += MAS_MEM[1]

	T20_in = S.Task('T20_in', length=1, delay_cost=1)
	S += T20_in >= 32
	T20_in += MM_in[0]

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 32
	T20_mem0 += MAS_MEM[6]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 32
	T20_mem1 += MAS_MEM[1]

	T21 = S.Task('T21', length=3, delay_cost=1)
	S += T21 >= 32
	T21 += MAS[1]

	T23 = S.Task('T23', length=14, delay_cost=1)
	S += T23 >= 32
	T23 += MM[0]

	T20 = S.Task('T20', length=14, delay_cost=1)
	S += T20 >= 33
	T20 += MM[0]

	T24_in = S.Task('T24_in', length=1, delay_cost=1)
	S += T24_in >= 33
	T24_in += MM_in[0]

	T24_mem0 = S.Task('T24_mem0', length=1, delay_cost=1)
	S += T24_mem0 >= 33
	T24_mem0 += MM_MEM[0]

	T24_mem1 = S.Task('T24_mem1', length=1, delay_cost=1)
	S += T24_mem1 >= 33
	T24_mem1 += MAS_MEM[1]

	T22_in = S.Task('T22_in', length=1, delay_cost=1)
	S += T22_in >= 34
	T22_in += MM_in[0]

	T22_mem0 = S.Task('T22_mem0', length=1, delay_cost=1)
	S += T22_mem0 >= 34
	T22_mem0 += MAS_MEM[2]

	T22_mem1 = S.Task('T22_mem1', length=1, delay_cost=1)
	S += T22_mem1 >= 34
	T22_mem1 += MAS_MEM[3]

	T24 = S.Task('T24', length=14, delay_cost=1)
	S += T24 >= 34
	T24 += MM[0]

	T22 = S.Task('T22', length=14, delay_cost=1)
	S += T22 >= 35
	T22 += MM[0]

	Z2_new_in = S.Task('Z2_new_in', length=1, delay_cost=1)
	S += Z2_new_in >= 36
	Z2_new_in += MM_in[0]

	Z2_new_mem0 = S.Task('Z2_new_mem0', length=1, delay_cost=1)
	S += Z2_new_mem0 >= 36
	Z2_new_mem0 += MAIN_MEM_r[0]

	Z2_new_mem1 = S.Task('Z2_new_mem1', length=1, delay_cost=1)
	S += Z2_new_mem1 >= 36
	Z2_new_mem1 += MM_MEM[1]

	Z2_new = S.Task('Z2_new', length=14, delay_cost=1)
	S += Z2_new >= 37
	Z2_new += MM[0]

	X1_new_in = S.Task('X1_new_in', length=1, delay_cost=1)
	S += X1_new_in >= 45
	X1_new_in += MAS_in[0]

	X1_new_mem0 = S.Task('X1_new_mem0', length=1, delay_cost=1)
	S += X1_new_mem0 >= 45
	X1_new_mem0 += MM_MEM[0]

	X1_new_mem1 = S.Task('X1_new_mem1', length=1, delay_cost=1)
	S += X1_new_mem1 >= 45
	X1_new_mem1 += MM_MEM[1]

	T25_in = S.Task('T25_in', length=1, delay_cost=1)
	S += T25_in >= 46
	T25_in += MAS_in[0]

	T25_mem0 = S.Task('T25_mem0', length=1, delay_cost=1)
	S += T25_mem0 >= 46
	T25_mem0 += MM_MEM[0]

	T25_mem1 = S.Task('T25_mem1', length=1, delay_cost=1)
	S += T25_mem1 >= 46
	T25_mem1 += MM_MEM[1]

	X1_new = S.Task('X1_new', length=3, delay_cost=1)
	S += X1_new >= 46
	X1_new += MAS[0]

	T25 = S.Task('T25', length=3, delay_cost=1)
	S += T25 >= 47
	T25 += MAS[0]

	X2_new_in = S.Task('X2_new_in', length=1, delay_cost=1)
	S += X2_new_in >= 48
	X2_new_in += MAS_in[0]

	X2_new_mem0 = S.Task('X2_new_mem0', length=1, delay_cost=1)
	S += X2_new_mem0 >= 48
	X2_new_mem0 += MM_MEM[0]

	X2_new_mem1 = S.Task('X2_new_mem1', length=1, delay_cost=1)
	S += X2_new_mem1 >= 48
	X2_new_mem1 += MM_MEM[1]

	X1_new_w = S.Task('X1_new_w', length=1, delay_cost=1)
	S += X1_new_w >= 49
	X1_new_w += MAIN_MEM_w

	X2_new = S.Task('X2_new', length=3, delay_cost=1)
	S += X2_new >= 49
	X2_new += MAS[0]

	Z1_new_in = S.Task('Z1_new_in', length=1, delay_cost=1)
	S += Z1_new_in >= 49
	Z1_new_in += MAS_in[0]

	Z1_new_mem0 = S.Task('Z1_new_mem0', length=1, delay_cost=1)
	S += Z1_new_mem0 >= 49
	Z1_new_mem0 += MM_MEM[0]

	Z1_new_mem1 = S.Task('Z1_new_mem1', length=1, delay_cost=1)
	S += Z1_new_mem1 >= 49
	Z1_new_mem1 += MAS_MEM[1]

	Z1_new = S.Task('Z1_new', length=3, delay_cost=1)
	S += Z1_new >= 50
	Z1_new += MAS[0]

	Z2_new_w = S.Task('Z2_new_w', length=1, delay_cost=1)
	S += Z2_new_w >= 51
	Z2_new_w += MAIN_MEM_w

	X2_new_w = S.Task('X2_new_w', length=1, delay_cost=1)
	S += X2_new_w >= 52
	X2_new_w += MAIN_MEM_w

	Z1_new_w = S.Task('Z1_new_w', length=1, delay_cost=1)
	S += Z1_new_w >= 53
	Z1_new_w += MAIN_MEM_w


	# new tasks
	T1 = S.Task('T1', length=14, delay_cost=1)
	T1 += alt(MM)
	T1_in = S.Task('T1_in', length=1, delay_cost=1)
	T1_in += alt(MM_in)
	S += T1_in*MM_in[0]<=T1*MM[0]
	S += T1<15

	T1_mem0 = S.Task('T1_mem0', length=1, delay_cost=1)
	T1_mem0 += MAIN_MEM_r[0]
	S += T1_mem0 <= T1

	T1_mem1 = S.Task('T1_mem1', length=1, delay_cost=1)
	T1_mem1 += MAIN_MEM_r[1]
	S += T1_mem1 <= T1

	T8 = S.Task('T8', length=14, delay_cost=1)
	T8 += alt(MM)
	T8_in = S.Task('T8_in', length=1, delay_cost=1)
	T8_in += alt(MM_in)
	S += T8_in*MM_in[0]<=T8*MM[0]
	S += T8<36

	T8_mem0 = S.Task('T8_mem0', length=1, delay_cost=1)
	T8_mem0 += MAIN_MEM_r[0]
	S += T8_mem0 <= T8

	T8_mem1 = S.Task('T8_mem1', length=1, delay_cost=1)
	T8_mem1 += alt(MM_MEM)
	S += (T1*MM[0])-1 < T8_mem1*MM_MEM[1]
	S += T8_mem1 <= T8

	T10 = S.Task('T10', length=14, delay_cost=1)
	T10 += alt(MM)
	T10_in = S.Task('T10_in', length=1, delay_cost=1)
	T10_in += alt(MM_in)
	S += T10_in*MM_in[0]<=T10*MM[0]
	S += T10<32

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	T10_mem0 += MAIN_MEM_r[0]
	S += T10_mem0 <= T10

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	T10_mem1 += MM_MEM[1]
	S += 17 < T10_mem1
	S += T10_mem1 <= T10

	T11 = S.Task('T11', length=14, delay_cost=1)
	T11 += alt(MM)
	T11_in = S.Task('T11_in', length=1, delay_cost=1)
	T11_in += alt(MM_in)
	S += T11_in*MM_in[0]<=T11*MM[0]
	S += T11<34

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	T11_mem0 += MAIN_MEM_r[0]
	S += T11_mem0 <= T11

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	T11_mem1 += MM_MEM[1]
	S += 17 < T11_mem1
	S += T11_mem1 <= T11

	T12 = S.Task('T12', length=3, delay_cost=1)
	T12 += alt(MAS)
	T12_in = S.Task('T12_in', length=1, delay_cost=1)
	T12_in += alt(MAS_in)
	S += T12_in*MAS_in[0]<=T12*MAS[0]

	S += T12_in*MAS_in[1]<=T12*MAS[1]

	S += T12_in*MAS_in[2]<=T12*MAS[2]

	S += T12_in*MAS_in[3]<=T12*MAS[3]

	S += T12<34

	T12_mem0 = S.Task('T12_mem0', length=1, delay_cost=1)
	T12_mem0 += MM_MEM[0]
	S += 16 < T12_mem0
	S += T12_mem0 <= T12

	T12_mem1 = S.Task('T12_mem1', length=1, delay_cost=1)
	T12_mem1 += MM_MEM[1]
	S += 15 < T12_mem1
	S += T12_mem1 <= T12

	T13 = S.Task('T13', length=3, delay_cost=1)
	T13 += alt(MAS)
	T13_in = S.Task('T13_in', length=1, delay_cost=1)
	T13_in += alt(MAS_in)
	S += T13_in*MAS_in[0]<=T13*MAS[0]

	S += T13_in*MAS_in[1]<=T13*MAS[1]

	S += T13_in*MAS_in[2]<=T13*MAS[2]

	S += T13_in*MAS_in[3]<=T13*MAS[3]

	S += T13<20

	T13_mem0 = S.Task('T13_mem0', length=1, delay_cost=1)
	T13_mem0 += MM_MEM[0]
	S += 16 < T13_mem0
	S += T13_mem0 <= T13

	T13_mem1 = S.Task('T13_mem1', length=1, delay_cost=1)
	T13_mem1 += MM_MEM[1]
	S += 15 < T13_mem1
	S += T13_mem1 <= T13

	T15 = S.Task('T15', length=3, delay_cost=1)
	T15 += alt(MAS)
	T15_in = S.Task('T15_in', length=1, delay_cost=1)
	T15_in += alt(MAS_in)
	S += T15_in*MAS_in[0]<=T15*MAS[0]

	S += T15_in*MAS_in[1]<=T15*MAS[1]

	S += T15_in*MAS_in[2]<=T15*MAS[2]

	S += T15_in*MAS_in[3]<=T15*MAS[3]

	S += T15<33

	T15_mem0 = S.Task('T15_mem0', length=1, delay_cost=1)
	T15_mem0 += MM_MEM[0]
	S += 19 < T15_mem0
	S += T15_mem0 <= T15

	T15_mem1 = S.Task('T15_mem1', length=1, delay_cost=1)
	T15_mem1 += MM_MEM[1]
	S += 19 < T15_mem1
	S += T15_mem1 <= T15

	T14 = S.Task('T14', length=14, delay_cost=1)
	T14 += alt(MM)
	T14_in = S.Task('T14_in', length=1, delay_cost=1)
	T14_in += alt(MM_in)
	S += T14_in*MM_in[0]<=T14*MM[0]
	S += T14<37

	T14_mem0 = S.Task('T14_mem0', length=1, delay_cost=1)
	T14_mem0 += alt(MAS_MEM)
	S += (T13*MAS[0])-1 < T14_mem0*MAS_MEM[0]
	S += (T13*MAS[1])-1 < T14_mem0*MAS_MEM[2]
	S += (T13*MAS[2])-1 < T14_mem0*MAS_MEM[4]
	S += (T13*MAS[3])-1 < T14_mem0*MAS_MEM[6]
	S += T14_mem0 <= T14

	T14_mem1 = S.Task('T14_mem1', length=1, delay_cost=1)
	T14_mem1 += alt(MAS_MEM)
	S += (T13*MAS[0])-1 < T14_mem1*MAS_MEM[1]
	S += (T13*MAS[1])-1 < T14_mem1*MAS_MEM[3]
	S += (T13*MAS[2])-1 < T14_mem1*MAS_MEM[5]
	S += (T13*MAS[3])-1 < T14_mem1*MAS_MEM[7]
	S += T14_mem1 <= T14

	T16 = S.Task('T16', length=14, delay_cost=1)
	T16 += alt(MM)
	T16_in = S.Task('T16_in', length=1, delay_cost=1)
	T16_in += alt(MM_in)
	S += T16_in*MM_in[0]<=T16*MM[0]
	S += T16<50

	T16_mem0 = S.Task('T16_mem0', length=1, delay_cost=1)
	T16_mem0 += alt(MM_MEM)
	S += (T1*MM[0])-1 < T16_mem0*MM_MEM[0]
	S += T16_mem0 <= T16

	T16_mem1 = S.Task('T16_mem1', length=1, delay_cost=1)
	T16_mem1 += alt(MM_MEM)
	S += (T8*MM[0])-1 < T16_mem1*MM_MEM[1]
	S += T16_mem1 <= T16

	T17 = S.Task('T17', length=14, delay_cost=1)
	T17 += alt(MM)
	T17_in = S.Task('T17_in', length=1, delay_cost=1)
	T17_in += alt(MM_in)
	S += T17_in*MM_in[0]<=T17*MM[0]
	S += T17<46

	T17_mem0 = S.Task('T17_mem0', length=1, delay_cost=1)
	T17_mem0 += alt(MM_MEM)
	S += (T8*MM[0])-1 < T17_mem0*MM_MEM[0]
	S += T17_mem0 <= T17

	T17_mem1 = S.Task('T17_mem1', length=1, delay_cost=1)
	T17_mem1 += alt(MAS_MEM)
	S += (T15*MAS[0])-1 < T17_mem1*MAS_MEM[1]
	S += (T15*MAS[1])-1 < T17_mem1*MAS_MEM[3]
	S += (T15*MAS[2])-1 < T17_mem1*MAS_MEM[5]
	S += (T15*MAS[3])-1 < T17_mem1*MAS_MEM[7]
	S += T17_mem1 <= T17

	T18 = S.Task('T18', length=3, delay_cost=1)
	T18 += alt(MAS)
	T18_in = S.Task('T18_in', length=1, delay_cost=1)
	T18_in += alt(MAS_in)
	S += T18_in*MAS_in[0]<=T18*MAS[0]

	S += T18_in*MAS_in[1]<=T18*MAS[1]

	S += T18_in*MAS_in[2]<=T18*MAS[2]

	S += T18_in*MAS_in[3]<=T18*MAS[3]

	S += T18<33

	T18_mem0 = S.Task('T18_mem0', length=1, delay_cost=1)
	T18_mem0 += MM_MEM[0]
	S += 18 < T18_mem0
	S += T18_mem0 <= T18

	T18_mem1 = S.Task('T18_mem1', length=1, delay_cost=1)
	T18_mem1 += MM_MEM[1]
	S += 28 < T18_mem1
	S += T18_mem1 <= T18

	T19 = S.Task('T19', length=3, delay_cost=1)
	T19 += alt(MAS)
	T19_in = S.Task('T19_in', length=1, delay_cost=1)
	T19_in += alt(MAS_in)
	S += T19_in*MAS_in[0]<=T19*MAS[0]

	S += T19_in*MAS_in[1]<=T19*MAS[1]

	S += T19_in*MAS_in[2]<=T19*MAS[2]

	S += T19_in*MAS_in[3]<=T19*MAS[3]

	S += T19<32

	T19_mem0 = S.Task('T19_mem0', length=1, delay_cost=1)
	T19_mem0 += MM_MEM[0]
	S += 18 < T19_mem0
	S += T19_mem0 <= T19

	T19_mem1 = S.Task('T19_mem1', length=1, delay_cost=1)
	T19_mem1 += MM_MEM[1]
	S += 28 < T19_mem1
	S += T19_mem1 <= T19

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage14MM1_stage3MAS4/EP_LADDERMUL/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

