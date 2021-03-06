import unittest

import OutputFunctions
import SecondaryBiasFinder
from SecondaryBiasFinder import SecondaryBias
from Director import Director, AnalysisBuilder
import Representation
from Bio import SeqRecord


class InductiveBiasFinderTest(unittest.TestCase):
    # make dictionary - sequence:sec value
    # or try with tuples
    # make sure tests that pass also fail if data is incorrect
    # test_sequences_dict = {"LGVQVKG": 2, "GSVQHAW": 1, "LFYQVFL": 1, "DEHQANI": 0, "SVNQGVY": 2, "FEIQDVP": 1,
    #                        "DVKQKDN": 1, "SLEQEIR": 0, "VEPQRIV": 2, "LAFQNHV": 1, "VKMQCLT": 1, "GKAQSGP": 0,
    #                        "YAMAFLP": 0, "VKGRTCT": 0}
    test_sequences_list = ["LGVQVKG", "GSVQHAW", "LFYQVFL", "DEHQANI", "SVNQGVY", "FEIQDVP",
                           "DVKQKDN", "VEPQRIV", "LLAQNGV", "VKMQCLT", "GKALSGP", "YAMAFLP", "VKGRTCT"]

    test_sequences_dict_one = {"LGVQVKG": 2, "GSVQHAW": 1, "LFYQVFL": 1, "DEHQANI": 0, "VKGRTCT": 0}
    test_sequences_list_one = ["LGVQVKG", "GSVQHAW", "LFYQVFL", "DEHQANI", "VKGRTCT"]

    test_sequences_dict_two = {"SVNQGVY": 2, "FEIQDVP": 1, "DVKQKDN": 1, "SLEQEIR": 0, "VKGRTCT": 0}
    test_sequences_list_two = ["SVNQGVY", "FEIQDVP", "DVKQKDN", "SLEQEIR", "VKGRTCT"]

    test_sequences_dict_three = {"VEPQRIV": 2, "LAFQNHV": 1, "VKMQCLT": 1, "GKAQSGP": 0, "YAMAFLP": 0, "VKGRTCT": 0}
    test_sequences_list_three = ["VEPQRIV", "LAFQNHV", "VKMQCLT", "GKAQSGP", "YAMAFLP", "VKGRTCT"]

    def test_concat_aa(self):
        for i1 in range(len(self.test_sequences_list)-1):
            if i1 < 3:
                for i2 in range(len(self.test_sequences_dict_one)-1):
                    seq_to_scan = SecondaryBias()
                    original_seq = self.test_sequences_list_one[i2]
                    seq_to_scan.seq = original_seq
                    append_sequence = self.test_sequences_list_one[i2 + 1]
                    for i3 in range(len(original_seq)-1):
                        seq_to_scan.bias_finder("Q")
                        self.assertEqual(seq_to_scan.one_away[17], self.test_sequences_dict_one[original_seq])
                        self.assertEqual(int(seq_to_scan.local_sequence[17]), self.test_sequences_dict_one[original_seq])
                        seq_to_scan = SecondaryBias()
                        seq_to_scan.seq = original_seq + append_sequence[0:i3]
            elif 2 < i1 < 10:
                for i2 in range(len(self.test_sequences_dict_two)-1):
                    seq_to_scan = SecondaryBias()
                    original_seq = self.test_sequences_list_two[i2]
                    seq_to_scan.seq = original_seq
                    append_sequence = self.test_sequences_list_two[i2 + 1]
                    for i3 in range(len(original_seq)-1):
                        seq_to_scan.bias_finder("Q")
                        self.assertEqual(seq_to_scan.two_away[17], self.test_sequences_dict_two[original_seq])
                        self.assertEqual(int(seq_to_scan.local_sequence[17]), self.test_sequences_dict_two[original_seq])
                        seq_to_scan = SecondaryBias()
                        seq_to_scan.seq = original_seq + append_sequence[0:i3]

            else:
                for i2 in range(len(self.test_sequences_dict_three)-1):
                    seq_to_scan = SecondaryBias()
                    original_seq = self.test_sequences_list_three[i2]
                    seq_to_scan.seq = original_seq
                    append_sequence = self.test_sequences_list_three[i2 + 1]
                    for i3 in range(len(original_seq)-1):
                        seq_to_scan.bias_finder("Q")
                        self.assertEqual(seq_to_scan.three_away[17], self.test_sequences_dict_three[original_seq])
                        self.assertEqual(int(seq_to_scan.local_sequence[17]), self.test_sequences_dict_three[original_seq])
                        seq_to_scan = SecondaryBias()
                        seq_to_scan.seq = original_seq + append_sequence[0:i3]

    def test_rev_concat_aa(self):
        for i1 in range(len(self.test_sequences_list)-1):
            if i1 < 3:
                for i2 in range(len(self.test_sequences_dict_one)-1):
                    seq_to_scan = SecondaryBias()
                    original_seq = self.test_sequences_list_one[i2]
                    seq_to_scan.seq = original_seq
                    append_sequence = self.test_sequences_list_one[i2 + 1]
                    for i3 in range(len(original_seq)-1):
                        seq_to_scan.bias_finder("Q")
                        self.assertEqual(seq_to_scan.one_away[17], self.test_sequences_dict_one[original_seq])
                        self.assertEqual(int(seq_to_scan.local_sequence[17]), self.test_sequences_dict_one[original_seq])
                        seq_to_scan = SecondaryBias()
                        holder = ""
                        for i in append_sequence[:i3]:
                            holder = i + holder
                        seq_to_scan.seq = holder + original_seq

            elif 2 < i1 < 10:
                for i2 in range(len(self.test_sequences_dict_two)-1):
                    seq_to_scan = SecondaryBias()
                    original_seq = self.test_sequences_list_two[i2]
                    seq_to_scan.seq = original_seq
                    append_sequence = self.test_sequences_list_two[i2 + 1]
                    for i3 in range(len(original_seq)-1):
                        seq_to_scan.bias_finder("Q")
                        self.assertEqual(seq_to_scan.two_away[17], self.test_sequences_dict_two[original_seq])
                        self.assertEqual(int(seq_to_scan.local_sequence[17]), self.test_sequences_dict_two[original_seq])
                        seq_to_scan = SecondaryBias()
                        holder = ""
                        for i in append_sequence[:i3]:
                            holder = i + holder
                        seq_to_scan.seq = holder + original_seq
            else:
                for i2 in range(len(self.test_sequences_dict_three)-1):
                    seq_to_scan = SecondaryBias()
                    original_seq = self.test_sequences_list_three[i2]
                    seq_to_scan.seq = original_seq
                    append_sequence = self.test_sequences_list_three[i2 + 1]
                    for i3 in range(len(original_seq)-1):
                        seq_to_scan.bias_finder("Q")
                        self.assertEqual(seq_to_scan.three_away[17], self.test_sequences_dict_three[original_seq])
                        self.assertEqual(int(seq_to_scan.local_sequence[17]), self.test_sequences_dict_three[original_seq])
                        seq_to_scan = SecondaryBias()
                        holder = ""
                        for i in append_sequence[:i3]:
                            holder = i + holder
                        seq_to_scan.seq = holder + original_seq

    def test_concat_whole_sequences(self):

        for i1 in range(len(self.test_sequences_list)-1):
            if i1 < 3:
                for i2 in range(len(self.test_sequences_dict_one)-1):
                    seq_to_scan = SecondaryBias()
                    original_seq = self.test_sequences_list_one[i2]
                    seq_to_scan.seq = original_seq
                    append_sequence = self.test_sequences_list_one[i2 + 1]
                    seq_to_scan.seq = original_seq + append_sequence
                    seq_to_scan.bias_finder("Q")
                    self.assertEqual(self.test_sequences_dict_one[original_seq] + self.test_sequences_dict_one[append_sequence], seq_to_scan.one_away[17], "full seq concat one away failed")
                    self.assertEqual(self.test_sequences_dict_one[original_seq] + self.test_sequences_dict_one[append_sequence], int(seq_to_scan.local_sequence[17]))

            elif 2 < i1 < 10:
                for i2 in range(len(self.test_sequences_dict_two)-1):
                    seq_to_scan = SecondaryBias()
                    original_seq = self.test_sequences_list_two[i2]
                    seq_to_scan.seq = original_seq
                    append_sequence = self.test_sequences_list_two[i2 + 1]
                    seq_to_scan.seq = original_seq + append_sequence
                    seq_to_scan.bias_finder("Q")
                    self.assertEqual(self.test_sequences_dict_two[original_seq] + self.test_sequences_dict_two[append_sequence], seq_to_scan.two_away[17], "full seq concat two away failed")
                    self.assertEqual(self.test_sequences_dict_two[original_seq] + self.test_sequences_dict_two[append_sequence], int(seq_to_scan.local_sequence[17]), )

            else:
                for i2 in range(len(self.test_sequences_dict_three)-1):
                    seq_to_scan = SecondaryBias()
                    original_seq = self.test_sequences_list_three[i2]
                    seq_to_scan.seq = original_seq
                    append_sequence = self.test_sequences_list_three[i2 + 1]
                    seq_to_scan.seq = original_seq + append_sequence
                    seq_to_scan.bias_finder("Q")
                    self.assertEqual(self.test_sequences_dict_three[original_seq] + self.test_sequences_dict_three[append_sequence], seq_to_scan.three_away[17], "full seq concat two away failed")
                    self.assertEqual(self.test_sequences_dict_three[original_seq] + self.test_sequences_dict_three[append_sequence], int(seq_to_scan.local_sequence[17]))


class BiasFinderTest(unittest.TestCase):
    primary_test = SecondaryBias()
    test_one_away = SecondaryBias()
    test_two_away = SecondaryBias()
    test_three_away = SecondaryBias()

    key1 = "I"
    test_one_away.seq = "IKAAESFLPSPVLRTDVMFLVPALKYNPLHRLLIQILGGHETMIQIGHAETATVKFEERLV" \
                             "ERIFDKRAGTSSLILIQIDYDEIQIWPGYSILRLGMPEKDEIQIAIITEMKRGAPHIQIQILDFGPA" \
                             "ISFKESWLDCVMGNCYNDIASEIKVRGSDLNKVGVRARKECGVATSPINAFINRLLSA" \
                             "TYSVGVNFLAVIQISTGIDKVHTNYDKA"

    key2 = "C"
    test_two_away.seq = "TTNIISELRCTQTCGNAMDNWMGEVLDGTPAFHFGVHCGDTAGPASKRFLLVCLEFSLR" \
                             "GYDLLVRLLLIKDEDANDVHCNQKCSQCCQKCMAHLALGPVTCSSSFNVHYSPGIGAL" \
                             "WACIQTCEIDYCIQPCKACVQSCEERSLKVIKADGITAKSFAPMPNGAVDPSTVEYMV" \
                             "KTLIVCLQTCYDENRTVRRFPEKAL"

    key3 = "S"
    test_three_away.seq = "YPSSALQGGSMSRFLSPTMLRVRASLGFLGINLLPWTLFVIAALPSKSDAQLSSTQPLSAMGME" \
                               "FIRANTESEINFVDKIHYAYHNLVVDPRKVDSEIAKERCKLLKSIVQVGSVTFATVPGDS" \
                               "YIGISSRSLMFVSEKNTGRELGNKCSAEQDDSSDQKNSGTAECGKLYSYEQWESTREGVDIIR" \
                               "KKTAVTHSNRQIPSVADHPLFLADAHEG"

    sequence1 = "QQQQQQQQQQQQQQQQQQ"
    sequence2 = "GWEQEWGGWEQEWGGWEQEWGGWEQEWG"
    sequence3 = "VTVQRSNFHQQKIRPQQPLGDKAHLLM"
    sequence4 = "CQQVKQDSHCCLQQQSTQLFQQQSERSQEIQMADIQTQ"
    sequence5 = "GQNQRWWYVTVQRSNFHQQKIRPQQPLGDKAHLLMQQMGGQQRAFYMPEQTQCFEYRI" \
                "DQCVWQEGFQEQAHAWPNVQKECQQVKQDSHCCLQQQSTLFQQQSERSQEIQMADIQTQ"
    sequence6 = "ADSFEWASDF"
    sequence7 = "WPNVQKECQQVKQDSHCCLQQQSTLFQ"
    sequence8 = "GVMWHDGTWDSAQHHFRQTY"
    sequence9 = "GQNQRWWYVTVQRSNFHQQKIRPQQPLGDKAHLLMQQMGGQQRAFYMPEQTQCFEYRI" \
                "DQCVWQEGFQEQAHAWPNVQKECQQVKQDSHCCLQQQSTLFQQQSERSQEIQMADIQ" \
                "TQCIGQNHQGVMWHDGTWDSAQHHFRQTYQYWWTPQLFVPYQDNRQAMNCQKLQAEVQ" \
                "SISQNTQKMPFPNQYQQKMDIKQIQQC"
    sequence10 = "VTVQRSNFHQQKIRPQQPLGDKAHLLM"

    seq_list = [sequence1, sequence2, sequence3, sequence4, sequence5,
                sequence6, sequence7, sequence8, sequence9, sequence10]

    list_q_content = [12, 4, 5, 10, 28, 0, 7, 1, 47]

    def test_run_pre_sec_bias1(self):
        self.test_one_away.primary_bias = "Q"
        self.test_one_away.seq_len = len(self.test_one_away.seq)
        self.test_one_away.bias_finder("Q")

    def test_run_pre_sec_bias2(self):
        self.test_two_away.primary_bias = "Q"
        self.test_two_away.seq_len = len(self.test_two_away.seq)
        self.test_two_away.bias_finder("Q")

    def test_run_pre_sec_bias3(self):
        self.test_three_away.primary_bias = "Q"
        self.test_three_away.seq_len = len(self.test_three_away.seq)
        self.test_three_away.bias_finder("Q")

    def test_secondary_bias_finder(self):
        keylist = ["I", "C", "S"]

        self.test_run_pre_sec_bias1()
        self.assertEqual(2, self.test_one_away.one_away[7] / self.test_one_away.Q_content)

        self.test_run_pre_sec_bias2()
        self.assertEqual(2, self.test_two_away.two_away[1] / self.test_two_away.Q_content)

        self.test_run_pre_sec_bias3()
        threeaway = self.test_three_away.three_away[15]
        self.assertEqual(2, (threeaway / self.test_three_away.Q_content))


class SequenceBiasIOTests(unittest.TestCase):

    def test_file_to_seqbias(self):
        seq_list = [["test1", "IKAAESFLPSPVLRTDVMFLVPALKYNPLHRLLIQILGGHETMIQIGHAETATVKFEERLVERIFDKRAGTSSLILIQIDYDEIQIWPGYSILRLGMPEKDEIQIAIITEMKRGAPHIQIQILDFGPAISFKESWLDCVMGNCYNDIASEIKVRGSDLNKVGVRARKECGVATSPINAFINRLLSATYSVGVNFLAVIQISTGIDKVHTNYDKA"],
                    ["test2", "TTNIISELRCTQTCGNAMDNWMGEVLDGTPAFHFGVHCGDTAGPASKRFLLVCLEFSLRGYDLLVRLLLIKDEDANDVHCNQKCSQCCQKCMAHLALGPVTCSSSFNVHYSPGIGALWACIQTCEIDYCIQPCKACVQSCEERSLKVIKADGITAKSFAPMPNGAVDPSTVEYMVKTLIVCLQTCYDENRTVRRFPEKAL"],
                    ["test3", "YPSSALQGGSMSRFLSPTMLRVRASLGFLGINLLPWTLFVIAALPSKSDAQLSSTQPLSAMGMEFIRANTESEINFVDKIHYAYHNLVVDPRKVDSEIAKERCKLLKSIVQVGSVTFATVPGDSYIGISSRSLMFVSEKNTGRELGNKCSAEQDDSSDQKNSGTAECGKLYSYEQWESTREGVDIIRKKTAVTHSNRQIPSVADHPLFLADAHEG"]]

        path_in = "/Users/coltongarelli/SequenceAnalyzer/PAM/Tests/Resources/SequenceBiasIOTestFile"

        director = Director()
        director.file_in_path = path_in
        director.start_up()
        seq_record_list = []
        for i in seq_list:
            seq_record_list.append(SeqRecord.SeqRecord(id=i[0], seq=i[1]))
        director.master_list = seq_record_list
        director.run_bias_analysis()
        for i in range(len(seq_list)):
            self.assertEqual(director.master_list[i].seq, seq_list[i][1])
            self.assertEqual(director.master_list[i].id, seq_list[i][0])

    def test_seqbias_to_file(self):
        list_q_content = [12, 4, 5, 10, 28, 0, 7, 1, 47]
        # one_away I = 16
        # two_away C =16
        seq_list = ["IKAAESFLPSPVLRTDVMFLVPALKYNPLHRLLIQILGGHETMIQIGHAETATVKFEERLVERIFDKRAGTSSLILIQIDYDEIQIWPGYSILRLGMPEKDEIQIAIITEMKRGAPHIQIQILDFGPAISFKESWLDCVMGNCYNDIASEIKVRGSDLNKVGVRARKECGVATSPINAFINRLLSATYSVGVNFLAVIQISTGIDKVHTNYDKA",
                    "TTNIISELRCTQTCGNAMDNWMGEVLDGTPAFHFGVHCGDTAGPASKRFLLVCLEFSLRGYDLLVRLLLIKDEDANDVHCNQKCSQCCQKCMAHLALGPVTCSSSFNVHYSPGIGALWACIQTCEIDYCIQPCKACVQSCEERSLKVIKADGITAKSFAPMPNGAVDPSTVEYMVKTLIVCLQTCYDENRTVRRFPEKAL",
                    "YPSSALQGGSMSRFLSPTMLRVRASLGFLGINLLPWTLFVIAALPSKSDAQLSSTQPLSAMGMEFIRANTESEINFVDKIHYAYHNLVVDPRKVDSEIAKERCKLLKSIVQVGSVTFATVPGDSYIGISSRSLMFVSEKNTGRELGNKCSAEQDDSSDQKNSGTAECGKLYSYEQWESTREGVDIIRKKTAVTHSNRQIPSVADHPLFLADAHEG"]

        seq_objs = []
        # test file in by checking read_file strings are equal
        # write one file manually and read it in, check to see it's equal to the read in from the exported file
        for i in range(len(seq_list)):
            seq = SecondaryBias()
            seq.initialize_sec_bias("tester", seq_list[i])
            seq.bias_finder("Q")
            seq_objs.append(seq)
        SecondaryBiasFinder.export_sec_bias_files(seq_objs)
        test_seq_list = SecondaryBiasFinder.processed_data_in("/Users/coltongarelli/Desktop/", "tester")
        for i in range(len(seq_objs)):
            self.assertEqual(seq_objs[i].id, test_seq_list[i].id)
            for i1 in range(0, 19):
                self.assertEqual(seq_objs[i].one_away[i1], test_seq_list[i].one_away[i1], )
                self.assertEqual(seq_objs[i].two_away[i1], test_seq_list[i].two_away[i1])
                self.assertEqual(seq_objs[i].three_away[i1], test_seq_list[i].three_away[i1])
                self.assertEqual(seq_objs[i].local_sequence[i1], test_seq_list[i].local_sequence[i1])


class CheckAATests(unittest.TestCase):
    # tests for checkaaentry method
    seq_1 = SecondaryBias()
    seq_1.seq = "SAQHHFRQTYQYWWTPQLFVPYQDNRQAMNCQKLQAEVQSISQNTQKMPFPNQYQQKMDIKQIQQC"
    seq_2 = SecondaryBias()
    seq_2.seq = "1"
    seq_3 = SecondaryBias()
    seq_3.seq = "1QCVWQEGFQEQAHA"
    seq_4 = SecondaryBias()
    seq_4.seq = "CCLQQQSTLFQQQSERSQEIQM3"
    seq_5 = SecondaryBias()
    seq_5.seq = "123453F13423"
    seq_6 = SecondaryBias()
    seq_6.seq = "ADSFEW@ASDF"
    seq_7 = SecondaryBias()
    seq_7.seq = "WPNVQKECQQVKQDSHCCLQQQSTLFQ*"
    seq_8 = SecondaryBias()
    seq_8.seq = "%GVMWHDGTWDSAQHHFRQTY"
    seq_9 = SecondaryBias()
    seq_9.seq = "ASSD SDS"
    seq_10 = SecondaryBias()
    seq_10.seq = "JJJJJJJJJJJ"
    seq_11 = SecondaryBias()
    seq_11.seq = "GQNQRWWYVTVQRSNFHQQKIRPQQPLGDKAHLLMQQMGGQQRAFYMPEQTQCFEYRI" \
                      "DQCVWQEGFQEQAHAWPNVQKECQQVKQDSHCCLQQQSTLFQQQSERSQEIQMADIQTQ" \
                      "CIGQNHQGVMWHDGTWDXSAQHHFRQTYQYWWTPQLFVPYQDNRQAMNCQKLQAEVQSIS" \
                      "QNTQKMPFPNQYQQKMDIKQIQQC"

    def test_check_aa_entry_pass(self):
        post_test = SecondaryBias()
        for i in range(10):
            post_test.seq = BiasFinderTest.seq_list[i]
            self.assertTrue(OutputFunctions.check_aa_entry(post_test.seq))

    def test_check_aa_entry_fail(self):
        self.assertFalse(OutputFunctions.check_aa_entry(self.seq_2.seq))
        self.assertFalse(OutputFunctions.check_aa_entry(self.seq_3.seq))
        self.assertFalse(OutputFunctions.check_aa_entry(self.seq_4.seq))
        self.assertFalse(OutputFunctions.check_aa_entry(self.seq_5.seq))
        self.assertFalse(OutputFunctions.check_aa_entry(self.seq_6.seq))
        self.assertFalse(OutputFunctions.check_aa_entry(self.seq_7.seq))
        self.assertFalse(OutputFunctions.check_aa_entry(self.seq_8.seq))
        self.assertFalse(OutputFunctions.check_aa_entry(self.seq_9.seq))
        self.assertFalse(OutputFunctions.check_aa_entry(self.seq_10.seq))
        self.assertFalse(OutputFunctions.check_aa_entry(self.seq_11.seq))


if __name__ == '__main__':

    unittest.main()
