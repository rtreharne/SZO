﻿
ALPHA_MULTILAYER

start_Model Version
	1	
end_Model Version

start_Model Parms
	2	0	
	-0.6740370401213671	T	-5.0	5.0	F	'Angle Offset'	F	F	0.0	0.0	100000.0	F	100.0	
	T	
	136.20217341793176	T	-200.0	500.0	F	'Roughness'	F	F	0.0	0.0	100000.0	F	100.0	
	F	
	20	
	'(none)'	
	1.3	
	5.0	
	20	
	
	'(none)'	
	0.0	
	0.5	
	3	
	
	'(none)'	
	0.0	
	0.0	
	0	
	
	T	
	3.107471016206523E-4	F	0.0	20.0	F	'# Back Reflections'	F	F	0.0	0.0	100000.0	F	100.0	
	100.0	F	0.0	100.0	F	'% 1st Reflection'	F	F	0.0	0.0	100000.0	F	100.0	
	
	F	
	3700.0	9000.0	
	T	
	'N,C,S'	
	T	
	F	
	20	
	0.0	F	0.0	50.0	F	'Bandwidth (eV)'	F	F	0.0	0.0	100000.0	F	100.0	
	9	
	F	
	T	
	T	
	T	
	6000.0	50000.0	
	F	
	5	
	F	
	F	
	'Ideal'	
	0.0	F	0.0	100.0	F	'% Thickness Non-uniformity'	F	F	0.0	0.0	100000.0	F	100.0	
	0.0	F	0.0	30.0	F	'Bandwidth (nm)'	F	F	0.0	0.0	100000.0	F	100.0	
	F	
	F	
	'All'	
	200.0	
	
	start_Ambient
		F	
		'(Not Specified)'	
		
	end_Ambient
	
	start_ScatteringFactor
		F	
		'(Not Specified)'	
		
	end_ScatteringFactor
	F	
	F	
	100.0	
	100.0	
	0.0	F	-5.0	5.0	F	'Wvl. Shift (nm)'	F	F	0.0	0.0	100000.0	F	100.0	
	1.0E-4	
	
	start_Simulation
		250.0	1000.0	5.0	45.0	75.0	10.0	100.0	F	0.5	
		F	
		1	
		0.0	F	0.0	10.0	F	'Angular Spread'	F	F	0.0	0.0	100000.0	F	100.0	
		'None'	
		0.0	F	-20.0	20.0	F	'#1'	F	F	0.0	0.0	100000.0	F	100.0	
		0.0	F	-20.0	20.0	F	'#2'	F	F	0.0	0.0	100000.0	F	100.0	
		0.0	F	-20.0	20.0	F	'#3'	F	F	0.0	0.0	100000.0	F	100.0	
		0.0	F	-20.0	20.0	F	'#4'	F	F	0.0	0.0	100000.0	F	100.0	
		0.0	F	-180.0	180.0	F	'Source Rot.'	F	F	0.0	0.0	100000.0	F	100.0	
		0.0	F	-180.0	180.0	F	'Receiver Rot.'	F	F	0.0	0.0	100000.0	F	100.0	
		F	
	end_Simulation
	
	start_MultiSamp
		0	0	
		
		start_DS Weighting
			
		end_DS Weighting
		
	end_MultiSamp
	
	start_ParmCoupling
		0	
		
		start_ParmCouplingFitParms
			0	
		end_ParmCouplingFitParms
		
	end_ParmCoupling
	100.0	
	'Standard Ellipsometric'	
	0	
	50	
	F	
	'(none)'	
	5	
	0.0	F	0.0	1000.0	F	'Smear Width'	F	F	0.0	0.0	100000.0	F	100.0	
	F	
	0	
	
	start_BW Conv
		'Gaussian'	
		0.0	F	0.0	1.0	F	'Exp. Relative Amp.'	F	F	0.0	0.0	100000.0	F	100.0	
		1.0	F	0.0	50.0	F	'Exp. Relative Width'	F	F	0.0	0.0	100000.0	F	100.0	
		F	
		0.0	F	0.0	30.0	F	'Bandwidth (nm) IR'	F	F	0.0	0.0	100000.0	F	100.0	
		1000.0	
		
	end_BW Conv
	
	start_Patterning
		F	
		0	
		0.0	F	0.0	100.0	F	'% Patterned'	F	F	0.0	0.0	100000.0	F	100.0	
		
	end_Patterning
	
	start_Color Calc
		F	
		346	163	560	301	
		0	1	2	'0'	
	end_Color Calc
	'(none)'	
	5	
	0.0	F	0.0	1000.0	F	'Smear Width #2'	F	F	0.0	0.0	100000.0	F	100.0	
	'(none)'	
	5	
	0.0	F	0.0	1000.0	F	'Smear Width #3'	F	F	0.0	0.0	100000.0	F	100.0	
	
	start_MultiModel
		0	2	
		
		50.0	F	0.0	100.0	F	'mWt1'	F	F	0.0	0.0	100000.0	F	100.0	
		50.0	F	0.0	100.0	F	'mWt2'	F	F	0.0	0.0	100000.0	F	100.0	
		
	end_MultiModel
	
end_Model Parms

start_Derived Parms
	T	
	
end_Derived Parms

start_Derived Parms 2
	'n'	1	6328.0	0.0	0.0	F	
	'k'	1	6328.0	0.0	0.0	F	
	
end_Derived Parms 2

start_Previous Results
	F	
	''	
	
end_Previous Results

start_Selected Options
	
	start_Options_Model Options
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		F	
		
	end_Options_Model Options
	
	start_Options_Fit Options
		T	
		F	
		F	
		F	
		F	
		
	end_Options_Fit Options
	
	start_Options_Other Options
		F	
		F	
		F	
		
	end_Options_Other Options
	
end_Selected Options

start_Model Structure
	
	start_Layer0
		4.0E7	F	-0.0	100000.0	F	'Substrate Thickness'	F	F	0.0	0.0	100000.0	F	100.0	
		'Layer'	'B-Spline'	'BSPLINE'	''	'B-Spline'	
		start_B-Spline Fit Parms
			25	0.73517906665802	5.14216947555542	F	
			F	
			1.5	
			0.0	
			0.3	
			F	
			F	
			0.0	F	0.0	1000.0	F	'UV Pole Amp (+0.1)'	F	F	0.0	0.0	100000.0	F	100.0	
			0.1	F	0.0	1000.0	F	'UV1 Pole E+'	F	F	0.0	0.0	100000.0	F	100.0	
			1.0	F	-10.0	100.0	F	'E Inf'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	0.0	1000.0	F	'IR Amp'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	0.0	100.0	F	'IR Br'	F	F	0.0	0.0	100000.0	F	100.0	
			T	
			F	
			F	
			'spline'	
			F	
			F	
			T	
			1.2	
			100000.0	5000.0	
			T	
			'(Not Specified)'	
			0	0.20000000298023224	F	1.0E-4	10.0	F	'Tie Off 0 {TieOff(1)-E}'	F	F	0.0	0.0	100000.0	F	100.0	
			1	0.20000000298023224	F	1.0E-4	10.0	F	'Tie Off 1 {TieOff(2)-E}'	F	F	0.0	0.0	100000.0	F	100.0	
			2	0.20000000298023224	F	1.0E-4	10.0	F	'Tie Off 2 {TieOff(3)-E}'	F	F	0.0	0.0	100000.0	F	100.0	
			3	0.20000000298023224	F	1.0E-4	10.0	F	'Tie Off 3 {TieOff(4)-E}'	F	F	0.0	0.0	100000.0	F	100.0	
			4	0.20000000298023224	F	1.0E-4	10.0	F	'Tie Off 4 (min-E)'	F	F	0.0	0.0	100000.0	F	100.0	
			5	0.5	F	1.0E-4	10.0	F	'Tie Off n+1 (max+E)'	F	F	0.0	0.0	100000.0	F	100.0	
			6	0.5	F	1.0E-4	10.0	F	'Tie Off n+2 {TieOff(n+1)+E}'	F	F	0.0	0.0	100000.0	F	100.0	
			7	1.0	F	1.0E-4	10.0	F	'Tie Off n+3 {TieOff(n+2)+E}'	F	F	0.0	0.0	100000.0	F	100.0	
			8	2.0	F	1.0E-4	10.0	F	'Tie Off n+4 {TieOff(n+3)+E}'	F	F	0.0	0.0	100000.0	F	100.0	
			9	4.0	F	1.0E-4	10.0	F	'Tie Off n+5 {TieOff(n+4)+E}'	F	F	0.0	0.0	100000.0	F	100.0	
			
		end_B-Spline Fit Parms
		
		start_B-Spline Nodes
			-0.76482093334198	-0.464820921421051	-0.16482093930244446	0.1351790726184845	0.43517905473709106	0.73517906665802	1.0499640703201294	1.3647490739822388	1.6795341968536377	1.994319200515747	2.3091042041778564	2.623889207839966	2.938674211502075	3.2534592151641846	3.568244218826294	3.8830294609069824	4.197814464569092	4.512599468231201	4.8273844718933105	5.14216947555542	5.442169666290283	5.742169380187988	6.042169570922852	6.342169284820557	6.64216947555542	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	
			0.0	F	-1000.0	1000.0	T	'spline_e2(-0.165)'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	T	'spline_e2(0.135)'	F	F	0.0	0.0	100000.0	F	100.0	
			-3.5637615148836975E-4	F	-1000.0	1000.0	T	'spline_e2(0.435)'	F	F	0.0	0.0	100000.0	F	100.0	
			-2.70824302360866E-4	F	-1000.0	1000.0	T	'spline_e2(0.735)'	T	F	0.0	0.0	100000.0	F	100.0	
			-1.8105617545825925E-4	F	-1000.0	1000.0	T	'spline_e2(1.050)'	T	F	0.0	0.0	100000.0	F	100.0	
			-1.4695057607839047E-4	F	-1000.0	1000.0	T	'spline_e2(1.365)'	T	F	0.0	0.0	100000.0	F	100.0	
			-1.1828921054334614E-4	F	-1000.0	1000.0	T	'spline_e2(1.680)'	T	F	0.0	0.0	100000.0	F	100.0	
			-1.021992083784024E-4	F	-1000.0	1000.0	T	'spline_e2(1.994)'	T	F	0.0	0.0	100000.0	F	100.0	
			-8.756133903295897E-5	F	-1000.0	1000.0	T	'spline_e2(2.309)'	T	F	0.0	0.0	100000.0	F	100.0	
			-7.918032086134706E-5	F	-1000.0	1000.0	T	'spline_e2(2.624)'	T	F	0.0	0.0	100000.0	F	100.0	
			-6.979549098788847E-5	F	-1000.0	1000.0	T	'spline_e2(2.939)'	T	F	0.0	0.0	100000.0	F	100.0	
			-6.64524570082014E-5	F	-1000.0	1000.0	T	'spline_e2(3.253)'	T	F	0.0	0.0	100000.0	F	100.0	
			-5.66983094671079E-5	F	-1000.0	1000.0	T	'spline_e2(3.568)'	T	F	0.0	0.0	100000.0	F	100.0	
			-5.7249906715783246E-5	F	-1000.0	1000.0	T	'spline_e2(3.883)'	T	F	0.0	0.0	100000.0	F	100.0	
			-8.508960571437801E-6	F	-1000.0	1000.0	T	'spline_e2(4.198)'	T	F	0.0	0.0	100000.0	F	100.0	
			3.330460562658539E-5	F	-1000.0	1000.0	T	'spline_e2(4.513)'	T	F	0.0	0.0	100000.0	F	100.0	
			-1.7048343221642574E-6	F	-1000.0	1000.0	T	'spline_e2(4.827)'	T	F	0.0	0.0	100000.0	F	100.0	
			3.472903037154407E-5	F	-1000.0	1000.0	T	'spline_e2(5.142)'	T	F	0.0	0.0	100000.0	F	100.0	
			6.945167036443635E-5	F	-1000.0	1000.0	T	'spline_e2(5.442)'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	T	'spline_e2(5.742)'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	T	'spline_e2(6.042)'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e2'	F	F	0.0	0.0	100000.0	F	100.0	
			
			0.0	F	-1000.0	1000.0	T	'spline_e1(-0.165)'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	T	'spline_e1(0.135)'	F	F	0.0	0.0	100000.0	F	100.0	
			2.6404541512650277	F	-1000.0	1000.0	T	'spline_e1(0.435)'	F	F	0.0	0.0	100000.0	F	100.0	
			2.670569628637061	F	-1000.0	1000.0	T	'spline_e1(0.735)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.702169296230875	F	-1000.0	1000.0	T	'spline_e1(1.050)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.735647054335075	F	-1000.0	1000.0	T	'spline_e1(1.365)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.7554228963394176	F	-1000.0	1000.0	T	'spline_e1(1.680)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.7788415539621747	F	-1000.0	1000.0	T	'spline_e1(1.994)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.8005850917857713	F	-1000.0	1000.0	T	'spline_e1(2.309)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.8259843128782762	F	-1000.0	1000.0	T	'spline_e1(2.624)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.857243037282777	F	-1000.0	1000.0	T	'spline_e1(2.939)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.884004226018431	F	-1000.0	1000.0	T	'spline_e1(3.253)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.9375372309170213	F	-1000.0	1000.0	T	'spline_e1(3.568)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.896967770049037	F	-1000.0	1000.0	T	'spline_e1(3.883)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.7649373554398937	F	-1000.0	1000.0	T	'spline_e1(4.198)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.8576058773938158	F	-1000.0	1000.0	T	'spline_e1(4.513)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.870180925535224	F	-1000.0	1000.0	T	'spline_e1(4.827)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.8982947256570535	F	-1000.0	1000.0	T	'spline_e1(5.142)'	T	F	0.0	0.0	100000.0	F	100.0	
			2.9250880776297032	F	-1000.0	1000.0	T	'spline_e1(5.442)'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	T	'spline_e1(5.742)'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	T	'spline_e1(6.042)'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			2.0	F	-1000.0	1000.0	F	'e1'	F	F	0.0	0.0	100000.0	F	100.0	
			
			
		end_B-Spline Nodes
		
		start_Node Positioning Ranges
			0	
		end_Node Positioning Ranges
		
		start_SL Parms
			0	1	
			
		end_SL Parms
		
	end_Layer0
	
	start_Layer1
		3273.353337617576	T	-10.0	100000.0	F	'Thickness # 1'	F	F	0.0	0.0	100000.0	F	100.0	
		'Layer'	'Gen-Osc'	'GENOSC'	''	'Gen-Osc'	
		start_Gen-Osc Misc Parms
			1	T	
			
		end_Gen-Osc Misc Parms
		
		start_Gen-Osc Fit Parms
			1	2.7748477406025143	T	0.0	10.0	F	'Einf'	F	F	0.0	0.0	100000.0	F	100.0	
			'PSemi-M0'	
			40.1395551970313	T	1.0E-4	1000.0	F	'Amp'	F	F	0.0	0.0	100000.0	F	100.0	
			0.23679832069011586	T	0.0	10.0	F	'Br'	F	F	0.0	0.0	100000.0	F	100.0	
			3.740984776864153	T	1.0E-4	15.0	F	'Eo'	F	F	0.0	0.0	100000.0	F	100.0	
			69.82023490974039	T	1.0E-4	100.0	F	'WR'	F	F	0.0	0.0	100000.0	F	100.0	
			0.999	T	0.0010	0.999	F	'PR'	F	F	0.0	0.0	100000.0	F	100.0	
			0.04191333571335926	T	0.0010	5.0	F	'AR'	F	F	0.0	0.0	100000.0	F	100.0	
			6.374653109356717	T	-1.0	10.0	F	'O2R'	F	F	0.0	0.0	100000.0	F	100.0	
			
		end_Gen-Osc Fit Parms
		
		start_Gen-Osc Grade Parms
			F	
			0.0	F	-1000.0	1000.0	F	'Grade 1'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	F	'Grade 2'	F	F	0.0	0.0	100000.0	F	100.0	
			F	
			0.0	F	-1000.0	1000.0	F	'Grade 1'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	F	'Grade 2'	F	F	0.0	0.0	100000.0	F	100.0	
			F	
			0.0	F	-1000.0	1000.0	F	'Grade 1'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	F	'Grade 2'	F	F	0.0	0.0	100000.0	F	100.0	
			F	
			0.0	F	-1000.0	1000.0	F	'Grade 1'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	F	'Grade 2'	F	F	0.0	0.0	100000.0	F	100.0	
			F	
			0.0	F	-1000.0	1000.0	F	'Grade 1'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	F	'Grade 2'	F	F	0.0	0.0	100000.0	F	100.0	
			F	
			0.0	F	-1000.0	1000.0	F	'Grade 1'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	F	'Grade 2'	F	F	0.0	0.0	100000.0	F	100.0	
			F	
			0.0	F	-1000.0	1000.0	F	'Grade 1'	F	F	0.0	0.0	100000.0	F	100.0	
			0.0	F	-1000.0	1000.0	F	'Grade 2'	F	F	0.0	0.0	100000.0	F	100.0	
			
		end_Gen-Osc Grade Parms
		
		start_Gen-Osc Permanent Poles
			330.041763269003	T	-1000.0	1000.0	F	'UV Pole Amp.'	F	F	0.0	0.0	100000.0	F	100.0	
			12.828698932365057	T	1.0E-8	15.0	F	'UV Pole En.'	F	F	0.0	0.0	100000.0	F	100.0	
			1.9270436943390665	T	-1000.0	1000.0	F	'IR Pole Amp.'	F	F	0.0	0.0	100000.0	F	100.0	
			
		end_Gen-Osc Permanent Poles
		
		start_SL Parms
			0	1	
			
		end_SL Parms
		
	end_Layer1
	
end_Model Structure
