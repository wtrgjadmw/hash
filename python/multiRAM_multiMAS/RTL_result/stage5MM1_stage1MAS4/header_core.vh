// ALU MM Memory
`define ALU_MM0_MEM_SIZE		256
`define ALU_MM0_MEM_ADDR_BITS	8

// ALU MAS Memory
`define ALU_MAS0_MEM_SIZE		128
`define ALU_MAS0_MEM_ADDR_BITS	7

`define ALU_MAS1_MEM_SIZE		128
`define ALU_MAS1_MEM_ADDR_BITS	7

`define ALU_MAS2_MEM_SIZE		128
`define ALU_MAS2_MEM_ADDR_BITS	7

`define ALU_MAS3_MEM_SIZE		128
`define ALU_MAS3_MEM_ADDR_BITS	7

// ALU MAIN Memory
`define ALU_MAIN_MEM_SIZE		128
`define ALU_MAIN_MEM_ADDR_BITS	7

// ===================================================================================
`define INST_CAL_MUX_BIT		4
`define INST_MAIN_MEM_MUX_BIT	3
`define INST_ADDR_MASK_BIT		1
`define INST_MM_MAS_VAL_BIT		1
`define INST_MAS_ISSUB_BIT		1
`define INST_WRITE_MUX_BIT		3
`define INST_WRITE_EN_BIT		1
`define INST_CONDKEY_BIT		2

// ALU Instructions Index
`define INDEX_MM0_READA		0
`define INDEX_MM0_MUXA		8
`define INDEX_MM0_READB		12
`define INDEX_MM0_MUXB		20
`define INDEX_MM0_VAL		24
`define INDEX_MM0_WRITE		25
`define INDEX_MM0_WE		33
`define INDEX_MAS0_READA	34
`define INDEX_MAS0_MUXA		41
`define INDEX_MAS0_READB		45
`define INDEX_MAS0_MUXB		52
`define INDEX_MAS0_ISSUB		56
`define INDEX_MAS0_VAL		57
`define INDEX_MAS0_WRITE		58
`define INDEX_MAS0_WE		65
`define INDEX_MAS1_READA		66
`define INDEX_MAS1_MUXA		73
`define INDEX_MAS1_READB		77
`define INDEX_MAS1_MUXB		84
`define INDEX_MAS1_ISSUB		88
`define INDEX_MAS1_VAL		89
`define INDEX_MAS1_WRITE		90
`define INDEX_MAS1_WE		97
`define INDEX_MAS2_READA		98
`define INDEX_MAS2_MUXA		105
`define INDEX_MAS2_READB		109
`define INDEX_MAS2_MUXB		116
`define INDEX_MAS2_ISSUB		120
`define INDEX_MAS2_VAL		121
`define INDEX_MAS2_WRITE		122
`define INDEX_MAS2_WE		129
`define INDEX_MAS3_READA		130
`define INDEX_MAS3_MUXA		137
`define INDEX_MAS3_READB		141
`define INDEX_MAS3_MUXB		148
`define INDEX_MAS3_ISSUB		152
`define INDEX_MAS3_VAL		153
`define INDEX_MAS3_WRITE		154
`define INDEX_MAS3_WE		161
`define INDEX_MAIN_READA		162
`define INDEX_MAIN_READB		169
`define INDEX_MAIN_WRITE		176
`define INDEX_MAIN_WE		183
`define INDEX_MAIN_WRITE_MUX		184
`define INDEX_MAIN_READ_MASKA		187
`define INDEX_MAIN_READ_MASKB		188
`define INDEX_MAIN_WRITE_MASK		189
`define INDEX_INST_CONT		192
`define INDEX_INST_END		193

`define ALU_INST_BITS		187
`define INST_BITS		    194
