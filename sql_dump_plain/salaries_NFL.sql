--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5
-- Dumped by pg_dump version 14.5

-- Started on 2022-11-30 19:38:26

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 213 (class 1259 OID 16451)
-- Name: coach; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.coach (
    coachid integer NOT NULL,
    firstname character varying(255),
    lastname character varying(255),
    salary integer,
    teamid integer
);


ALTER TABLE public.coach OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16417)
-- Name: mascot; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mascot (
    mascotid integer NOT NULL,
    name character varying(255),
    salary integer,
    teamid integer
);


ALTER TABLE public.mascot OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16434)
-- Name: player; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player (
    playerid integer NOT NULL,
    firstname character varying(255),
    lastname character varying(255),
    salary integer,
    positionid integer,
    teamid integer
);


ALTER TABLE public.player OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16427)
-- Name: position; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."position" (
    positionid integer NOT NULL,
    positionname character varying(255),
    abbr character varying(255)
);


ALTER TABLE public."position" OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16410)
-- Name: team; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.team (
    location character varying(255),
    name character varying(255),
    teamid integer NOT NULL,
    color1 character varying(255),
    color2 character varying(255)
);


ALTER TABLE public.team OWNER TO postgres;

--
-- TOC entry 3336 (class 0 OID 16451)
-- Dependencies: 213
-- Data for Name: coach; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.coach (coachid, firstname, lastname, salary, teamid) FROM stdin;
1	Sean	McVay	16000000	19
2	Bill	Belichick	12500000	22
3	Pete	Carroll	11000000	29
4	Kyle	Shanahan	9500000	28
5	John	Harbaugh	9000000	3
6	Franck	Reich	9000000	14
7	Matt	Rhule	8500000	5
8	Mike	Tomlin	8000000	27
9	Andy	Reid	8000000	16
10	Sean	McDermott	8000000	4
11	Ron	Rivera	7000000	32
12	Nick	Sirianni	6500000	26
13	Kliff	Kingsbury	5500000	1
14	Matt	LaFleur	5000000	12
15	Robert	Saleh	5000000	25
16	Zac	Taylor	4500000	7
17	Mike	McCarthy	4000000	9
18	Nathaniel	Hackett	4000000	10
19	Kevin	Stefanski	4000000	8
20	Mike	Vrabel	3000000	31
21	Brandon	Staley	3000000	18
22	Dan	Campbell	3000000	11
23	Arthur	Smith	2500000	2
24	Todd	Bowles	2500000	30
25	Dennis	Allen	2500000	23
26	Doug	Pederson	2000000	15
27	Josh	McDaniels	2000000	17
28	Mike	McDaniel	2000000	20
29	Kevin	OConnell	1500000	21
30	Matt	Eberflus	1500000	6
31	Brian	Daboll	1500000	24
32	Lovie	Smith	1000000	13
\.


--
-- TOC entry 3333 (class 0 OID 16417)
-- Dependencies: 210
-- Data for Name: mascot; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mascot (mascotid, name, salary, teamid) FROM stdin;
1	Poe	60000	3
2	Billy Buffalo	60000	4
3	Who Dey	55000	7
4	Chomps	55000	8
5	Miles	60000	10
6	Toro	60000	13
7	Blue	50000	14
8	Jaxson de Ville	60000	15
9	Wold	60000	16
10	Raider Rusher	50000	17
11	T.D.	55000	20
12	Pat Patriot	65000	22
13	Steely McBeam	60000	27
14	T-Rac	60000	31
15	Big Red	60000	1
16	Freddie Falcon	50000	2
17	Sir Purr	50000	5
18	Staley Da Bear	60000	6
19	Rowdy	65000	9
20	Roary	60000	11
21	Rampage	50000	19
22	Viktor	50000	21
23	Gumbo	50000	23
24	Swoop	60000	26
25	Sourdough Sam	60000	28
26	Blitz	50000	29
27	Captain Fear	50000	30
\.


--
-- TOC entry 3335 (class 0 OID 16434)
-- Dependencies: 212
-- Data for Name: player; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.player (playerid, firstname, lastname, salary, positionid, teamid) FROM stdin;
1	Kyler	Murray	46100000	1	1
2	Budda	Baker	14750000	12	1
3	DeAndre	Hopkins	27250000	4	1
4	D.J.	Humphries	17254510	6	1
5	Justin	Pugh	8995000	7	1
6	Jalen	Thompson	12000000	12	1
7	Zach	Ertz	10550000	5	1
8	Rodney	Hudson	10000000	8	1
9	Robbie	Anderson	14750000	4	1
10	J.J.	Watt	14000000	14	1
11	Jake	Matthews	14000000	6	2
12	Grady.	Jarrett	16823333	15	2
13	Kyle	Pitts	8227624	5	2
14	Younghoe	Koo	4850000	19	2
15	Drake	London	5383617	4	2
16	Marcus	Mariota	9375000	1	2
17	Chris	Lindstrom	3681822	7	2
18	A.J.	Terrell	3576437	11	2
19	Casey	Hayward	5500000	11	2
20	Calvin	Ridley	2725178	4	2
21	Ronnie	Stanley	19750000	6	3
22	Marlon	Humphrey	19500000	11	3
23	Marcus	Williams	14000000	13	3
24	Mark	Andrews	14000000	5	3
25	Marcus	Peters	14000000	11	3
26	Justin	Tucker	6000000	19	3
27	Kevin	Zeitler	7500000	9	3
28	Tyus	Bowser	5500000	16	3
29	Michael	Pierce	5500000	15	3
30	Kyle	Hamilton	4063771	13	3
31	Josh	Allen	43005667	1	4
32	Von	Miller	20000000	14	4
33	Stefon	Diggs	24000000	4	4
34	TreDavious	White	17250000	11	4
35	Dion	Dawkins	14575000	6	4
36	Dawson	Knox	13000000	5	4
37	Matt	Milano	10375000	16	4
38	Taron	Johnson	8000000	11	4
39	Ed	Oliver	4891289	15	4
40	Taylor	Moton	17811500	10	4
41	D.J.	Moore	20628000	4	5
42	Shaq	Thompson	13608250	16	5
43	Donte	Jackson	11726667	11	5
44	Baker	Mayfield	8170745	1	5
45	Sam	Darnold	7561929	1	5
46	Ikem	Ekwonu	6892013	5	5
47	Austin	Corbett	8750000	9	5
48	Derrick	Brown	5905351	15	5
49	Jaycee	Horn	5278037	11	5
50	C.J.	Henderson	5129005	11	5
51	Eddie	Jackson	14600000	13	6
52	Cody	Whitechair	10250000	9	6
53	Justin	Fields	4717989	1	6
54	Roquan	Smith	4619292	18	6
55	Alex	Leatherwood	3597891	10	6
56	Justin	Jones	6000000	15	6
57	NKeal	Harry	2524587	4	6
58	Kyler	Gordon	2170732	11	6
59	Teven	Jenkins	2096962	7	6
60	Lucas	Patrick	4000000	7	6
61	Trey	Hendrickson	15000000	14	7
62	D.J.	Reader	13250000	15	7
63	Joe	Mixon	12000000	2	7
64	Tyler	Boyd	10750000	4	7
65	Sam	Hubbard	10000000	14	7
66	Joe	Burrow	9047534	1	7
67	Alex	Cappa	8750000	9	7
68	JaMarr	Chase	7704910	4	7
69	B.J.	Hill	10000000	15	7
70	Mike	Hilton	6000000	11	7
71	Deshaun	Watson	46000000	1	8
72	Myles	Garret	25000000	14	8
73	Denzel	Ward	20100000	11	8
74	Amari	Cooper	20000000	4	8
75	Deion	Jones	14250000	17	8
76	Wyatt	Teller	14200000	7	8
77	David	Njoku	13687500	5	8
78	Joel	Bitonio	16000000	9	8
79	Jack	Conklin	14000000	10	8
80	Nick	Chubb	12200000	2	8
81	Dak	Prescott	1600000	1	9
82	Ezekiel	Elliott	12400000	2	9
83	DeMarcus	Lawrence	3000000	14	9
84	Dalton	Schultz	10931000	5	9
85	Anthony	Barr	1250000	16	9
86	Noah	Brown	1035000	4	9
87	Sam	Williams	705000	15	9
88	Brett	Maher	911387	19	9
89	Markquese	Bell	705000	12	9
90	Trysten	Hill	1160208	15	9
91	Justin	Simmons	15100000	13	10
92	Russell	Wilson	2000000	1	10
93	Bradley	Chubb	12716000	16	10
94	Graham	Glasgow	3100000	9	10
95	Courtland	Sutton	1500000	4	10
96	Patrick	Surtain	825000	11	10
97	Brandon	McManus	3000000	19	10
98	Jerry	Jeudy	1991179	4	10
99	DJ	Jones	1035000	15	10
100	Josey	Jewell	1500000	17	10
101	Jared	Goff	10650000	1	11
102	Taylor	Decker	8750000	6	11
103	Jeff	Okudah	895000	11	11
104	Frank	Ragnow	2751529	8	11
105	Michael	Brockers	3000000	15	11
106	TJ	Hockenson	965000	5	11
107	Aiden	Hutchinson	705000	14	11
108	Penei	Sewell	825000	10	11
109	Jamaal	Williams	3750000	2	11
110	Will	Harris	2510000	12	11
111	Aaron	Rodgers	1150000	1	12
112	David	Bakhtiari	1120000	6	12
113	Preston	Smith	1150000	16	12
114	Kenny	Clark	1035000	15	12
115	Dean	Lowry	5000000	14	12
116	Aaron	Jones	1000000	2	12
117	Mason	Crosby	2250000	19	12
118	Allen	Lazard	3986000	4	12
119	Darnell	Savage	2201958	12	12
120	Josh	Myers	913643	8	12
121	Laremy	Tunsil	1035000	6	13
122	Brandin	Cooks	1168889	4	13
123	Eric	Murray	1035000	13	13
124	Tytus	Howard	2162121	10	13
125	Kyle	Allen	1750000	1	13
126	MJ	Stewart	1500000	12	13
127	Kaimi	Fairbairn	1035000	19	13
128	Maliek	Collins	1500000	15	13
129	Christian	Kirksey	2000000	17	13
130	Jerry	Hughes	2000000	14	13
131	Matt	Ryan	5205882	1	14
132	DeForest	Buckner	11000000	15	14
133	Yannick	Ngakoue	5000000	14	14
134	Braden	Smith	5567000	10	14
135	Shaquille	Leonard	6916000	17	14
136	Quenton	Nelson	4000000	7	14
137	Ryan	Kelly	3500000	8	14
138	Nyheim	Hines	3300000	2	14
139	Zaire	Franklin	1100000	16	14
140	Michael	Pittman	1392986	4	14
141	Rayshawn	Jenkins	7000000	13	15
142	Evan	Engram	5250000	5	15
143	Marvin	Jones	4950000	4	15
144	Brandon	Scherff	1500000	7	15
145	Cam	Robinson	2000000	6	15
146	Josh	Allen	3596269	16	15
147	Darious	Williams	5500000	11	15
148	Dawuane	Smoot	3850000	14	15
149	Foyesade	Oluokun	1500000	17	15
150	Logan	Cooke	2080000	20	15
151	Patrick	Mahomes	1500000	1	16
152	Chris	Jones	3750000	15	16
153	Orlando	Brown	16662000	6	16
154	Frank	Clark	3311111	14	16
155	Marquez	ValdesScantling	2560000	4	16
156	Justin	Reid	1035000	13	16
157	Clyde	EdwardsHelaire	1593779	2	16
158	Harrison	Butker	1163611	19	16
159	Travis	Kelce	2893333	5	16
160	Nick	Bolton	925183	16	16
161	Derek	Carr	17400000	1	17
162	Davante	Adams	3500000	4	17
163	Darren	Waller	11000000	5	17
164	Clelin	Ferrell	4771476	14	17
165	Kolton	Miller	3275000	6	17
166	Bilal	Nichols	2375000	15	17
167	Denzel	Perryman	3000000	17	17
168	Josh	Jacobs	2122281	2	17
169	Johnathan	Abram	2062527	13	17
170	Anthony	Averett	1950000	11	17
171	Keenan	Allen	16500000	4	18
172	Corey	Linsley	9000000	8	18
173	Michael	Davis	7000000	11	18
174	Khalil	Mack	4050000	16	18
175	Justin	Herbert	3026250	1	18
176	Austin	Ekeler	5500000	2	18
177	Sebastian	Joseph	2500000	14	18
178	Austin	Johnson	1750000	15	18
179	Dustin	Hopkins	1120000	19	18
180	Tre	McKitty	877539	5	18
181	Aaron	Donald	1500000	15	19
182	Jalen	Ramsey	15000000	11	19
183	Cooper	Kupp	10000000	4	19
184	Matthew	Stafford	1500000	1	19
185	AShawn	Robinson	6500000	14	19
186	Rob	Havenstein	1500000	10	19
187	Tyler	Higbee	1500000	5	19
188	Taylor	Rapp	2540000	12	19
189	Matt	Gay	2540000	19	19
190	Brian	Allen	1000000	8	19
191	Emmanuel	Ogbah	4000000	14	20
192	Mike	Gesicki	10931000	5	20
193	Jerome	Baker	6580000	17	20
194	Xavien	Howard	1035000	11	20
195	Tua	Tagovailoa	895000	1	20
196	Teddy	Bridgewater	4500000	1	20
197	Tyreek	Hill	1035000	4	20
198	Connor	Williams	1035000	8	20
199	Chase	Edmonds	2000000	2	20
200	Eric	Rowe	2500000	12	20
201	Kirk	Cousins	5000000	1	21
202	Eric	Kendricks	9150000	17	21
203	Danielle	Hunter	1400000	16	21
204	Dalvin	Cook	8300000	2	21
205	Brian	ONeill	4400000	10	21
206	Adam	Thielen	4253529	4	21
207	Dalvin	Tomlinson	4900000	14	21
208	Harrison	Smith	2950000	13	21
209	Garrett	Bradbury	2251755	8	21
210	Greg	Joseph	2433000	19	21
211	Matt	Judon	11000000	16	22
212	Hunter	Henry	9000000	5	22
213	Nelson	Agholor	9000000	4	22
214	Davon	Godchaux	1500000	15	22
215	Jonathan	Jones	5400000	11	22
216	Mac	Jones	1368471	1	22
217	Adrian	Phillips	1120000	13	22
218	Mack	Wilson	2540000	17	22
219	David	Andrews	1120000	8	22
220	Nick	Folk	1120000	19	22
221	Michael	Thomas	1035000	4	23
222	Cameron	Jordan	1120000	14	23
223	Ryan	Ramczyk	1035000	10	23
224	David	Onyemata	1035000	15	23
225	Alvin	Kamara	1035000	2	23
226	Demario	Davis	1120000	17	23
227	Wil	Lutz	3400000	19	23
228	Taysom	Hill	1100000	5	23
229	Jameis	Winston	1200000	1	23
230	James	Hurst	1120000	6	23
231	Kenny	Golladay	13000000	4	24
232	Leonard	Williams	1120000	14	24
233	Adoree	Jackson	1035000	11	24
234	Andrew	Thomas	2550508	6	24
235	Daniel	Jones	965000	1	24
236	Saquon	Barkley	7217000	2	24
237	Kayvon	Thibodeaux	705000	16	24
238	Nick	Gates	2050000	8	24
239	Graham	Gano	1120000	19	24
240	Julian	Love	2540000	13	24
241	C.J.	Mosley	17000000	17	25
242	John	Franklin-Myers	13750000	14	25
243	Carl	Lawson	15000000	14	25
244	Laken	Tomlinson	12500000	6	25
245	Corey	Davis	12500000	4	25
246	Zach	Wilson	8787670	1	25
247	Ahmad	Gardner	83627000	11	25
248	D.J.	Reed	11000000	11	25
249	Quinnen	Williams	8132343	15	25
250	George	Fant	9100000	10	25
251	A.J.	Brown	25000000	4	26
252	Lane	Johnson	18000000	10	26
253	Darius	Slay	16683333	11	26
254	Jordan	Mailata	16000000	6	26
255	Haason	Reddick	15000000	16	26
256	Dallas	Goedert	14250000	5	26
257	Robert	Quinn	14000000	14	26
258	Fletcher	Cox	14000000	15	26
259	Brandon	Graham	13333333	14	26
260	Josh	Sweat	13333333	14	26
261	T.J.	Watt	28002750	16	27
262	Minkah	Fitzpatrick	18403059	13	27
263	Diontae	Johnson	18355000	4	27
264	Cameron	Heyward	16400000	15	27
265	Chuks	Okorafor	9750000	10	27
266	James	Daniels	8833333	7	27
267	Myles	Jack	8000000	17	27
268	Larry	Ogunjobi	8000000	15	27
269	Mitchell	Trubisky	7142500	1	27
270	Mason	Cole	5250000	8	27
271	Deebo	Samuel	23850000	4	28
272	Trent	Williams	23010000	6	28
273	Fred	Warner	19045000	18	28
274	Arik	Armstead	17000000	14	28
275	Christian	McCaffrey	16015875	2	28
276	George	Kittle	15000000	5	28
277	Charvarius	Ward	13500000	11	28
278	Jimmie	Ward	9500000	13	28
279	Trey	Lance	8526319	1	28
280	Nick	Bosa	8387966	14	28
281	D.K.	Metcalf	24000000	4	29
282	Jamal	Adams	17645000	12	29
283	Tyler	Lockett	17250000	4	29
284	Quandre	Diggs	13000000	12	29
285	Uchenna	Nwosu	9527500	18	29
286	Shelby	Harris	9000000	15	29
287	Will	Dissly	8000000	5	29
288	Gabe	Jackson	7525000	9	29
289	Poona	Ford	6172500	14	29
290	Rashaad	Penny	5750000	2	29
291	Chris	Godwin	20000000	4	30
292	Vita	Vea	17750000	15	30
293	Shaquil	Barrett	17000000	16	30
294	Mike	Evans	16500000	4	30
295	Donovan	Smith	15500000	6	30
296	Tom	Brady	15000000	1	30
297	Carlton	Davis	14833333	11	30
298	Ryan	Jensen	13000000	8	30
299	Lavonte	David	12500000	17	30
300	Russell	Gage	10000000	4	30
301	Ryan	Tannehill	29500000	1	31
302	Harold	Landry	17500000	16	31
303	Bud	Dupree	16500000	16	31
304	Robert	Woods	16250000	4	31
305	Taylor	Lewan	16000000	6	31
306	Zach	Cunningham	14500000	17	31
307	Kevin	Byard	14100000	13	31
308	Derrick	Henry	12500000	2	31
309	Amani	Hooker	10000000	12	31
310	Denico	Autry	7166667	14	31
311	Terry	McLaurin	22788000	4	32
312	Jonathan	Allen	18000000	15	32
313	William	Jackson	13500000	11	32
314	Charles	Leno	12333333	6	32
315	Curtis	Samuel	11500000	4	32
316	Chase	Roullier	10125000	8	32
317	Kendall	Fuller	10000000	11	32
318	Chase	Young	8640899	14	32
319	Logan	Thomas	8021667	5	32
320	Andrew	Norwell	5000000	9	32
\.


--
-- TOC entry 3334 (class 0 OID 16427)
-- Dependencies: 211
-- Data for Name: position; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."position" (positionid, positionname, abbr) FROM stdin;
1	Quarterback	QB
2	Running Back	RB
3	Full Back	FB
4	Wide Receiver	WR
5	Tight End	TE
6	Left Tackle	LT
7	Left Guard	LG
8	Center	C
9	Right Guard	RG
10	Right Tackle	RT
11	Cornerback	CB
12	Strong Safety	SS
13	Free Safety	FS
14	Defensive End	DE
15	Defensive Tackle	DT
16	Outside Linebacker	OLB
17	Inside Linebacker	ILB
18	Linebacker	LB
19	Kicker	K
20	Punter	P
\.


--
-- TOC entry 3332 (class 0 OID 16410)
-- Dependencies: 209
-- Data for Name: team; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.team (location, name, teamid, color1, color2) FROM stdin;
Arizona	Cardinals	1	Red	Black
Atlanta	Falcons	2	Red	Black
Buffalo	Bills	4	Red	Blue
Carolina	Panthers	5	Black	Blue
Chicago	Bears	6	Blue	Orange
Cincinnati	Bengals	7	Black	Orange
Cleveland	Browns	8	Brown	Orange
Dallas	Cowboys	9	Blue	White
Detroit	Lions	11	Blue	Silver
GreenBay	Packers	12	Green	Yellow
Houston	Texans	13	Red	White
Indianapolis	Colts	14	Blue	Gray
KansasCity	Chiefs	16	Red	Gold
LasVegas	Raiders	17	Black	Silver
LosAngeles	Chargers	18	Blue	Yellow
LosAngeles	Rams	19	Blue	Gold
NewEngland	Patriots	22	Red	Blue
NewOrleans	Saints	23	Black	Gold
NewYork	Giants	24	Red	Blue
NewYork	Jets	25	Green	White
Philadelphia	Eagles	26	Green	Black
Pittsburgh	Steelers	27	Black	Gold
Seattle	Seahawks	29	Green	Blue
TampaBay	Buccaneers	30	Black	Red
Tennessee	Titans	31	Blue	Red
Washington	Commanders	32	Red	Gold
SanFrancisco	49ers	28	Red	Gold
Denver	Broncos	10	Red	Orange
Miami	Dolphins	20	Blue	Orange
Jacksonville	Jaguars	15	Cyan	Gold
Baltimore	Ravens	3	Magenta	Black
Minnesota	Vikings	21	Magenta	Gold
\.


--
-- TOC entry 3188 (class 2606 OID 16457)
-- Name: coach coach_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coach
    ADD CONSTRAINT coach_pkey PRIMARY KEY (coachid);


--
-- TOC entry 3182 (class 2606 OID 16421)
-- Name: mascot mascot_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mascot
    ADD CONSTRAINT mascot_pkey PRIMARY KEY (mascotid);


--
-- TOC entry 3186 (class 2606 OID 16440)
-- Name: player player_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_pkey PRIMARY KEY (playerid);


--
-- TOC entry 3184 (class 2606 OID 16433)
-- Name: position position_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."position"
    ADD CONSTRAINT position_pkey PRIMARY KEY (positionid);


--
-- TOC entry 3180 (class 2606 OID 16416)
-- Name: team team_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team
    ADD CONSTRAINT team_pkey PRIMARY KEY (teamid);


--
-- TOC entry 3192 (class 2606 OID 16458)
-- Name: coach coach_teamid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coach
    ADD CONSTRAINT coach_teamid_fkey FOREIGN KEY (teamid) REFERENCES public.team(teamid);


--
-- TOC entry 3189 (class 2606 OID 16422)
-- Name: mascot mascot_teamid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mascot
    ADD CONSTRAINT mascot_teamid_fkey FOREIGN KEY (teamid) REFERENCES public.team(teamid);


--
-- TOC entry 3190 (class 2606 OID 16441)
-- Name: player player_positionid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_positionid_fkey FOREIGN KEY (positionid) REFERENCES public."position"(positionid);


--
-- TOC entry 3191 (class 2606 OID 16446)
-- Name: player player_teamid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_teamid_fkey FOREIGN KEY (teamid) REFERENCES public.team(teamid);


-- Completed on 2022-11-30 19:38:27

--
-- PostgreSQL database dump complete
--

