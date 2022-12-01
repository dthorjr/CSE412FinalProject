PGDMP         %            
    z            salaries_NFL    14.5    14.5                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16409    salaries_NFL    DATABASE     r   CREATE DATABASE "salaries_NFL" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE "salaries_NFL";
                postgres    false            �            1259    16451    coach    TABLE     �   CREATE TABLE public.coach (
    coachid integer NOT NULL,
    firstname character varying(255),
    lastname character varying(255),
    salary integer,
    teamid integer
);
    DROP TABLE public.coach;
       public         heap    postgres    false            �            1259    16417    mascot    TABLE     �   CREATE TABLE public.mascot (
    mascotid integer NOT NULL,
    name character varying(255),
    salary integer,
    teamid integer
);
    DROP TABLE public.mascot;
       public         heap    postgres    false            �            1259    16434    player    TABLE     �   CREATE TABLE public.player (
    playerid integer NOT NULL,
    firstname character varying(255),
    lastname character varying(255),
    salary integer,
    positionid integer,
    teamid integer
);
    DROP TABLE public.player;
       public         heap    postgres    false            �            1259    16427    position    TABLE     �   CREATE TABLE public."position" (
    positionid integer NOT NULL,
    positionname character varying(255),
    abbr character varying(255)
);
    DROP TABLE public."position";
       public         heap    postgres    false            �            1259    16410    team    TABLE     �   CREATE TABLE public.team (
    location character varying(255),
    name character varying(255),
    teamid integer NOT NULL,
    color1 character varying(255),
    color2 character varying(255)
);
    DROP TABLE public.team;
       public         heap    postgres    false                      0    16451    coach 
   TABLE DATA           M   COPY public.coach (coachid, firstname, lastname, salary, teamid) FROM stdin;
    public          postgres    false    213   |                 0    16417    mascot 
   TABLE DATA           @   COPY public.mascot (mascotid, name, salary, teamid) FROM stdin;
    public          postgres    false    210   h                 0    16434    player 
   TABLE DATA           [   COPY public.player (playerid, firstname, lastname, salary, positionid, teamid) FROM stdin;
    public          postgres    false    212   �                 0    16427    position 
   TABLE DATA           D   COPY public."position" (positionid, positionname, abbr) FROM stdin;
    public          postgres    false    211   .                 0    16410    team 
   TABLE DATA           F   COPY public.team (location, name, teamid, color1, color2) FROM stdin;
    public          postgres    false    209   x/       t           2606    16457    coach coach_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.coach
    ADD CONSTRAINT coach_pkey PRIMARY KEY (coachid);
 :   ALTER TABLE ONLY public.coach DROP CONSTRAINT coach_pkey;
       public            postgres    false    213            n           2606    16421    mascot mascot_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.mascot
    ADD CONSTRAINT mascot_pkey PRIMARY KEY (mascotid);
 <   ALTER TABLE ONLY public.mascot DROP CONSTRAINT mascot_pkey;
       public            postgres    false    210            r           2606    16440    player player_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_pkey PRIMARY KEY (playerid);
 <   ALTER TABLE ONLY public.player DROP CONSTRAINT player_pkey;
       public            postgres    false    212            p           2606    16433    position position_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."position"
    ADD CONSTRAINT position_pkey PRIMARY KEY (positionid);
 B   ALTER TABLE ONLY public."position" DROP CONSTRAINT position_pkey;
       public            postgres    false    211            l           2606    16416    team team_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.team
    ADD CONSTRAINT team_pkey PRIMARY KEY (teamid);
 8   ALTER TABLE ONLY public.team DROP CONSTRAINT team_pkey;
       public            postgres    false    209            x           2606    16458    coach coach_teamid_fkey    FK CONSTRAINT     x   ALTER TABLE ONLY public.coach
    ADD CONSTRAINT coach_teamid_fkey FOREIGN KEY (teamid) REFERENCES public.team(teamid);
 A   ALTER TABLE ONLY public.coach DROP CONSTRAINT coach_teamid_fkey;
       public          postgres    false    209    3180    213            u           2606    16422    mascot mascot_teamid_fkey    FK CONSTRAINT     z   ALTER TABLE ONLY public.mascot
    ADD CONSTRAINT mascot_teamid_fkey FOREIGN KEY (teamid) REFERENCES public.team(teamid);
 C   ALTER TABLE ONLY public.mascot DROP CONSTRAINT mascot_teamid_fkey;
       public          postgres    false    210    209    3180            v           2606    16441    player player_positionid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_positionid_fkey FOREIGN KEY (positionid) REFERENCES public."position"(positionid);
 G   ALTER TABLE ONLY public.player DROP CONSTRAINT player_positionid_fkey;
       public          postgres    false    3184    212    211            w           2606    16446    player player_teamid_fkey    FK CONSTRAINT     z   ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_teamid_fkey FOREIGN KEY (teamid) REFERENCES public.team(teamid);
 C   ALTER TABLE ONLY public.player DROP CONSTRAINT player_teamid_fkey;
       public          postgres    false    209    212    3180               �  x�MSˎ�@<wLD�YE�z���\�06#�g���i�U�U�TJZ8�rʢ�P����*��V�7 �Π�O�+�I��D��D�	F��j���@X��ݵ�I�õ�raŘ����MN��V���(�N���Ţ�bG}S���F[(�}�%ll3N:��7eHQȹW��X1�	��Y8���0�@�6%����ZY�1��\���;~�tA	)��~�/F�0k�lvV��Jծ�H�2�%kx��q�E-G��ǚ�����S"�&{�Y+ý�7Ů����zpCU�.�v7���h������8'[�G�&"�9� 1M�������=yļ6<!'��oa�	�i`��խ@�Ha���6�(���(2ػ�ʷ�(��0"X�(r>������{�9�"46�+&�/T�c笝Pp$��yq_yC3t+�a<u�g����V���W��jI>���D�Z�?         N  x�EQ�n�0>�O�j�?�ĤIH�Ep�%��Fkq��b��ψ�E�!_��ǖ�'Y�bTPض�E1].�%�'é!�13���1�uC]?x`�)�lk�"#��@.P�s(��@�|'���3�M�FY5��)��Dm��Jmk�D9�q�$G)��,��T�ף��,��=q�2�j4���΅ѝ'WL�����0�2�1\Ei^Pf�u���[ݞ��-0q�ub?�`+E�d1ݚYl�`5�y8�
J�׳7�B��H�9(IT��v���f�U
��{� ��,����������D}���J����4]Q��^��xv��,��Z���7�}8~~�~.�1��            x�eZ�r�8�}��e/ ���V�+i�;��*N�5��\��9����uDwG�$I �y�d��x8�vO�8��(��菐B���bn[#.���+��
qeχv��ν��(�:�x	�W_���;{hY�L(�����S7���v't�Ѓ��Ľ�� ^w��~t>�e�Wk�O�ى�q�-dV��U �xv�`O�bˏe�1����Y�ۑ�Z+uO��a�	H�C��[�hg?��D~�%ݎ�=}��8ZzZ��!+�v���M�Q�<�U^
FJ�7۝���9Q��چ�J\���G7�XlU�B�k���q3�?���h
�
h-.��x��8�� 
�%����6�j�ھEU������F\�#yМ>��
��̣y����=wm+:mYk^T.��a��_&3*��_%�3|����//�A7�����V~�aP��^p��O�"��O��w�,�\�`{�7�*���x����n�<��������^��#���T#������kǍ]`ZT����3�����2SE]K��a�;q�S��E�UJ�DyV��/�?��d�����O�W�v���e����2�#G��r�EO�q����V��E�����x�/,3yX�	@�2�CnŐ��$3�{��y�xh#�[��>��R72�y�<+3<w��Ǒ�LRV�\F����(&�T��F��2/;���"
�il����l��l����+	.�=������в��$Bh%^�����lp�)�{{��O7�B�&�p�A�8�!v��7�¿!T�*Ǳ�����>��MV�$7 m��������ZgEX+�t�,j#oU2o,��mۭvZ��4�ʱ���C�ځ³<�x��pe-놎��)��l�r��8�	����x��8~:ׂK��K���s�n �������kz��8�H���4� �ѭ��r:d��%5 ��˽|���(�6u�2�8o8�L��JJ���@�U�dV}��p�=[�R�+b�T�Q���׺� �x���b멨 �t7����z�?������S4��WR{�^��w�
# ��A��iQ�Y���F\p��5V�����Zr�i(�}tte�;3T��+e>�����Q�ru��e@I��?h�H��f��8?�@!�����I��\YFg�*��Dd�j��ƃX"�V|���ϔ��!$!0M>��E�}v`���������}7�J��W���N'�����>���q���i�t.��=�G\�l1(�'���h>G;�JD^�a�d�\^6��gQ���.`��0��pg��et�"P�������+�_ 5�^��uV�p �� 1ԓA�F��(��.���uA� >H�i@���8!�|��y��[��!�_���Qm�b8@eg`���x��bYiI�1\`U�uE<��=M[%�$��æn{s�"g
��
;��S+^�iZ�T��,T�U�V�k�>���͓p`��\�����-�81�_ވ����� X#�yK�}������m�������y��W�u�N��a���S��skHC��X��g/��v�����h����޽�n�M�x�GE�5�᥉ ����a�6��b���BC��/~��ٙG)��K�ao9��.���%� ������L~���������	IO��92(8�9븶��^Bȹ˞4��H	%�BY|t��#2���b4D2`�T��rt�7��͍�u����7j�h�ІE	9��|�-4�A����y�%�Ӊ\Ҁ!���$�9��	
x8v}��[ �}�|q{��Zst\���6�AL�(<JpB��9nr�r� 5����~g�NEZ�{�xpZR#� t�����ny�?ő��BÝ}g��E�9K�A�!� Dm7�)��l������=.��;t:��!i�U��՗�f��Q ��o�ժx��)�?�"��׭ٻ��0dQ2���U��)W,ugj���@.VM����(�_�(��Z��E�0^��? vN�>����ig;蔎�(R�ڠ�� ��K�lFRWlPf�h���8d"J��T��9Aa|.����&&(�x�z؎��*O==��~$Y6�k'�L���iG��*m�P�N4�����*��u��r�(@R�o�"I�b6��1A"��=87�"6�ay��q'{���!X�?
 L ����ģ6G{�g��j�Z��]�8�	�<���;�D)�-ķ�J��]P�Ox,��B�^=��UC����Ǘ�&�|��)�a��϶k��Bk��\���;�sHɪA;�P���\�C��'�6IU(ZN�- �G����2
m$�Y�VUp��T���>JI�����2�����P�x�r%Zt���D���1�+��؞�Ը	3�M~Y+v#� ��BG_��fXA����X��� ��Z���Qd'��K����G1�{����5�`�]9�4<x�F	F�4�L>X�=��-:ϰ�43`	�ہ^�I\-Ҁ�ˤ��9F���\$����K�/=�b����6�ږRLh�Y4�(E�+n�=�b�}���jD�{Bؾ_H���b��C&:�!�/�*�� �7,!�9���Ȅ�&a��p� 
<A���k�XG�r���?*T8��gDMŪ�s/b��0��/�]��2�%i����5?���&�D�j�}�P!��WC�w+�ʼA:ܻn�fm��tԨ��W���?�{����֜�a����-1���R\�3�����v5�͡��MpO{k���n�41L�x_�I��t��K�?Eү^�$ʒ���6�u��I��ÐƶE�@~��&[��lBN-('4�7cPS:�g˰3hoЄ��E+�.�$'���س��K4L�Сn�H���	� 4�O>�1db�ـ�n�� &n����l��G��B'��`��WK�.㳙�S�x��4�̫���ңu|�;�>X�f9v2YU	/��HU�7h¨bbU�6������X��h��JV<<v'4Ƚ��u�J�a�4�ΣS��0.DWy����|&��F��8y��k���5�AEe�S���U���4���֢P��q��Б����;
��K�B{���wL�ڣM�Ҁ=<��Cy�q�~M��D�4�5�u���?'f}S4�$��A��)8p����2�ai߆�=�ɬ26�a$��z�q�s�*P�D�P��k����8O�E��x����q����@�amG�p�^2�D�F#c}�<�CX:Pe�0oѹ����X��yR�I��F&��w5�]���4��(�rHy�
�*t��Y�.����!U��F�ޫ�Swv�hF2���R<�@x��1s~$
�b<֤q�'�"
(��������K��~&��XmȤ'p���yjY����2i�қ�{���a0�%��]s��T��EdO��<�"F���٦k]��#��d�LK\�Rۨ�����@�a�mW,��^7$Ichht�E�/aytkݸE�a�_h�P�/}O�f�X�����&��t��y��p��襧�UJ��N��2&�*''k��*oP��y�J�>X�=���-I�4��AM�� ����kq�ۉBѯ�oR��P�O|�
���Ok���J�n��V�=��H�d�C��t���нA�eEV5�dU�E�d֎.�ȚdQ&ּ��:�Ʋ2�hV�"�m�F�
N����@A>�&�o��p��<O�@M##�o�y���b�Nן�d0��8�u�=H��9L���ϻ�Dl�Ǩ'�o��$���;c�pN���B�*c�A�Gv���TJ���|���}c�ǿP�H��&���l�is	����*C/
0�V*&i��.�Zy������3��Ad�)#��Yw8t���ڻ�h�/��s�iu�� �̘N=�
��u�T\>�J|y 	"�M�s}�7�s����E�T�A>�E��4ߥ�o���%R��o;�=s�N���o�0���gl��Zv?�(���S��F)D�Cx��W��؟RhP�ߖ�V���G�ݡ2B� �  �(̯��]ų9��;��*���a\	���K��]�_(�/ڪ�.��"��&�;m!.6)}SBӬ�Kf���}��TY�r¸�Rêu�z��Z5��=�2$��+�{�p�L���m^|#�T�U�u�:����`Y�����A�!uU7�O� �c���G
�S젽gȠ����~'��<�2���Z�\
F���b>�����Pi/�a�-�y���ğx\�8C��f���z������]e�Eǃ���q������4	*�k�~��+O��6�f)�@
��E�|���^q-[����6)����-I�<-�a��<N����r�c\�������һ���j�Q����a�a:���$4��F����&:���8�o0ϢT��F�0����_�����R"         �   x�]��j�0E�w��_P"7ϭ���Ȃl�q�q*jP�B����B�r��r����:�����sB1�`�6�(	D&�b���,Z�[�$�X��E�
J�?]��*�5*�\�|�gT�6(�R���-R6~)� ��ɒ�b&s]*�Ú�1MHĨ�}xǺ�����IxM��G
O�ȸc����Z��X��y!�k�U�p��v��Om�7��}�x!�p��q�x��0~x��7"�K�i&         #  x�US]s�0|V~�	�G>Z�8�2�i�3}Q�hpl�6pܯ?�	���Y�jW�ǖ��0E[�F� �*`�0�'c�P{�'T���;lr��P��V�E����Q�k�Vd�JW�c)<B��'<[ԥ`�s�=��`��^+�HLI/k�bi�|\�*����i.F��[�^0�ְ�%�,i�`V'����	^�u����?x'��9�i��[���ލ��_�`�x�ܡ������K�[��/ �i'� ��F��+��������[oK��N��Wh�X3l�[ww%/X�&����Q�qjk����˲����B��h�up�+	��7j��~;�f*��#<b�e����Dk��}mY�Ɠؗd��}���J�DX�y/��KA�o�>`X���)t;���L��59G[�!a��{ ��U�˰֩�kP�g��lP?�����z��ox�g�eA�
����;j�⊱f��0��x:���B:�O�|X�sH�0��n�'�<�ƊW<Q�+,)<�fz+ٌ�_y/9�G�U%>~$I�w�C@     