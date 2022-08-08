# textanalysis
Scripts for analysing Classical Chinese texts
\>>> a, b, c, d = create_common_char_docs('round1_1')

0: HFZ1_.txt

1: HFZ2_.txt

2: ZCG-Chu_.txt

3: ZCG-Han_.txt

4: ZCG-Qi_.txt

5: ZGC-Chu_.txt

6: ZGC-Han_.txt

7: ZGC-Qin_.txt

8: ZGC-Speaking_.txt

9: ZGC-Wei_.txt

10: ZGC-Yan_.txt

11: ZGC-Zhao_.txt



ONLY COMMON CHARACTERS RESULT

\>>> read_docs_into_cv_cosine_similarity_matrix(b)

array([[1.    , 0.94030219, 0.83796946, 0.85735379, 0.86656184,

​    0.83796946, 0.83796946, 0.87121443, 0.86879612, 0.84474541,

​    0.90000076, 0.858338 ],

​    [0.94030219, 1.    , 0.89582766, 0.91997935, 0.91210795,

​    0.89582766, 0.89582766, 0.90750584, 0.90004889, 0.88643006,

​    0.92307963, 0.90324771],

​    [0.83796946, 0.89582766, 1.    , 0.94388662, 0.96405808,

​    \1.    , 1.    , 0.97798938, 0.86987408, 0.97198238,

​    0.96639303, 0.97084835],

​    [0.85735379, 0.91997935, 0.94388662, 1.    , 0.93421094,

​    0.94388662, 0.94388662, 0.94809498, 0.89866643, 0.94736234,

​    0.94242406, 0.93873764],

​    [0.86656184, 0.91210795, 0.96405808, 0.93421094, 1.    ,

​    0.96405808, 0.96405808, 0.97349477, 0.91972762, 0.96786452,

​    0.96041056, 0.9722406 ],

​    [0.83796946, 0.89582766, 1.    , 0.94388662, 0.96405808,

​    \1.    , 1.    , 0.97798938, 0.86987408, 0.97198238,

​    0.96639303, 0.97084835],

​    [0.83796946, 0.89582766, 1.    , 0.94388662, 0.96405808,

​    \1.    , 1.    , 0.97798938, 0.86987408, 0.97198238,

​    0.96639303, 0.97084835],

​    [0.87121443, 0.90750584, 0.97798938, 0.94809498, 0.97349477,

​    0.97798938, 0.97798938, 1.    , 0.89438438, 0.97262958,

​    0.97618874, 0.9747628 ],

​    [0.86879612, 0.90004889, 0.86987408, 0.89866643, 0.91972762,

​    0.86987408, 0.86987408, 0.89438438, 1.    , 0.88690998,

​    0.88730686, 0.90205005],

​    [0.84474541, 0.88643006, 0.97198238, 0.94736234, 0.96786452,

​    0.97198238, 0.97198238, 0.97262958, 0.88690998, 1.    ,

​    0.96261638, 0.9782483 ],

​    [0.90000076, 0.92307963, 0.96639303, 0.94242406, 0.96041056,

​    0.96639303, 0.96639303, 0.97618874, 0.88730686, 0.96261638,

​    \1.    , 0.96277148],

​    [0.858338 , 0.90324771, 0.97084835, 0.93873764, 0.9722406 ,

​    0.97084835, 0.97084835, 0.9747628 , 0.90205005, 0.9782483 ,

​    0.96277148, 1.    ]])



\>>> read_docs_into_dendrogram(b)

![image-20210907165111535](/Users/xingjing/Library/Application Support/typora-user-images/image-20210907165111535.png)

(8 is ZGC-Speaking, and by this method arguably seems most similiar to the Han texts)



USING ORIGINAL DOCUMENTS

\>>> bb = create_original_docs('round1_1')

0: HFZ1_.txt

1: HFZ2_.txt

2: ZCG-Chu_.txt

3: ZCG-Han_.txt

4: ZCG-Qi_.txt

5: ZGC-Chu_.txt

6: ZGC-Han_.txt

7: ZGC-Qin_.txt

8: ZGC-Speaking_.txt

9: ZGC-Wei_.txt

10: ZGC-Yan_.txt

11: ZGC-Zhao_.txt



\>>> read_docs_into_cv_cosine_similarity_matrix(bb)

array([[1.    , 0.92436078, 0.70897974, 0.6817494 , 0.76331458,

​    0.70897974, 0.70897974, 0.73495921, 0.82468911, 0.70807182,

​    0.76409778, 0.72535049],

​    [0.92436078, 1.    , 0.77014251, 0.73996353, 0.80953098,

​    0.77014251, 0.77014251, 0.77217983, 0.84833942, 0.74567839,

​    0.78720588, 0.76832223],

​    [0.70897974, 0.77014251, 1.    , 0.88838365, 0.91306734,

​    \1.    , 1.    , 0.94126306, 0.67878842, 0.91582577,

​    0.89887928, 0.90662469],

​    [0.6817494 , 0.73996353, 0.88838365, 1.    , 0.85073063,

​    0.88838365, 0.88838365, 0.90692191, 0.6581186 , 0.90111178,

​    0.84774706, 0.86682099],

​    [0.76331458, 0.80953098, 0.91306734, 0.85073063, 1.    ,

​    0.91306734, 0.91306734, 0.92564137, 0.7482022 , 0.90060632,

​    0.92415029, 0.93109339],

​    [0.70897974, 0.77014251, 1.    , 0.88838365, 0.91306734,

​    \1.    , 1.    , 0.94126306, 0.67878842, 0.91582577,

​    0.89887928, 0.90662469],

​    [0.70897974, 0.77014251, 1.    , 0.88838365, 0.91306734,

​    \1.    , 1.    , 0.94126306, 0.67878842, 0.91582577,

​    0.89887928, 0.90662469],

​    [0.73495921, 0.77217983, 0.94126306, 0.90692191, 0.92564137,

​    0.94126306, 0.94126306, 1.    , 0.68709838, 0.94777792,

​    0.92780703, 0.94774157],

​    [0.82468911, 0.84833942, 0.67878842, 0.6581186 , 0.7482022 ,

​    0.67878842, 0.67878842, 0.68709838, 1.    , 0.67398133,

​    0.69055246, 0.69979352],

​    [0.70807182, 0.74567839, 0.91582577, 0.90111178, 0.90060632,

​    0.91582577, 0.91582577, 0.94777792, 0.67398133, 1.    ,

​    0.89115719, 0.93667288],

​    [0.76409778, 0.78720588, 0.89887928, 0.84774706, 0.92415029,

​    0.89887928, 0.89887928, 0.92780703, 0.69055246, 0.89115719,

​    \1.    , 0.92940482],

​    [0.72535049, 0.76832223, 0.90662469, 0.86682099, 0.93109339,

​    0.90662469, 0.90662469, 0.94774157, 0.69979352, 0.93667288,

​    0.92940482, 1.    ]])

\>>> read_docs_into_tfidf_cosine_similarity_matrix(bb)

array([[1.    , 0.89387205, 0.57497785, 0.53777296, 0.61772628,

​    0.57497785, 0.57497785, 0.59646151, 0.77371583, 0.57797411,

​    0.61558398, 0.58309889],

​    [0.89387205, 1.    , 0.64051243, 0.59982061, 0.67201928,

​    0.64051243, 0.64051243, 0.64198866, 0.78071297, 0.6237281 ,

​    0.64877519, 0.63358715],

​    [0.57497785, 0.64051243, 1.    , 0.84970606, 0.88111147,

​    \1.    , 1.    , 0.91642675, 0.49450745, 0.89387444,

​    0.86516468, 0.87371385],

​    [0.53777296, 0.59982061, 0.84970606, 1.    , 0.80532101,

​    0.84970606, 0.84970606, 0.87253141, 0.46721436, 0.87161845,

​    0.79869442, 0.82342491],

​    [0.61772628, 0.67201928, 0.88111147, 0.80532101, 1.    ,

​    0.88111147, 0.88111147, 0.89615313, 0.54357772, 0.87213063,

​    0.89222714, 0.8991575 ],

​    [0.57497785, 0.64051243, 1.    , 0.84970606, 0.88111147,

​    \1.    , 1.    , 0.91642675, 0.49450745, 0.89387444,

​    0.86516468, 0.87371385],

​    [0.57497785, 0.64051243, 1.    , 0.84970606, 0.88111147,

​    \1.    , 1.    , 0.91642675, 0.49450745, 0.89387444,

​    0.86516468, 0.87371385],

​    [0.59646151, 0.64198866, 0.91642675, 0.87253141, 0.89615313,

​    0.91642675, 0.91642675, 1.    , 0.49912957, 0.93269389,

​    0.89979518, 0.92665186],

​    [0.77371583, 0.78071297, 0.49450745, 0.46721436, 0.54357772,

​    0.49450745, 0.49450745, 0.49912957, 1.    , 0.49298104,

​    0.49863433, 0.5046223 ],

​    [0.57797411, 0.6237281 , 0.89387444, 0.87161845, 0.87213063,

​    0.89387444, 0.89387444, 0.93269389, 0.49298104, 1.    ,

​    0.86357563, 0.91600144],

​    [0.61558398, 0.64877519, 0.86516468, 0.79869442, 0.89222714,

​    0.86516468, 0.86516468, 0.89979518, 0.49863433, 0.86357563,

​    \1.    , 0.90176572],

​    [0.58309889, 0.63358715, 0.87371385, 0.82342491, 0.8991575 ,

​    0.87371385, 0.87371385, 0.92665186, 0.5046223 , 0.91600144,

​    0.90176572, 1.    ]])

\>>> read_docs_into_dendrogram(bb)

![image-20210907165452183](/Users/xingjing/Library/Application Support/typora-user-images/image-20210907165452183.png)

it can be seen that if you include the rest of the topic words, speaking to king in zheng may be closer in topics to the other chapters in the book (all the numbers but 0, 1, 8). but using only common characters (particles etc) type of usage shows that the way the author of Speaking writes uses similiar frequencies of such base words/structures in the essay.



common characters btw

\>>> d

{'厚', '莫', '制', '人', '焉', '乎', '宜', '！', '百', '中', '使', '大', '如', '以', '？', '上', '，', '「', '令', '哉', '可', '今', '：', '西', '事', '士', '未', '昔', '能', '而', '主', '公', '成', '是', '信', '者', '善', '所', '失', '得', '王', '言', '弱', '重', '有', '入', '故', '天', '命', '合', '城', '外', '忠', '侯', '皆', '少', '明', '功', '取', '之', '身', '相', '不', '君', '下', '我', '亦', '患', '免', '小', '一', '也', '；', '氏', '尊', '十', '朝', '名', '此', '遂', '然', '千', '弗', '用', '行', '伐', '、', '立', '先', '知', '女', '任', '矣', '」', '日', '子', '曰', '必', '吾', '。', '夫', '心', '攻', '其', '非', '利', '臣', '求', '欲', '乘', '兵', '\n', '反'}



MORE ON DENDROGRAM (IMPORTANT)

dendrogram axis is not similiarity - it's the euclidean distance metric. each axis can be seen as a word, and the frequency of the word (if CountVectorizer is used) is the distance in the axis. with higher dimensional data, the euclidean metric suffers from the curse of dimensionality (distance between random pairs of points are all roughly the same). hence pick only common words. we also assume when doing cosine similarity or such that the words are "orthogonal" i.e. all equally independent from each other. this assumption is not correct of course, but looking at the kinds of words that appear in common characters above, the common characters might have a higher proportion of such "independent" words eg. with different grammatical functions, on different topics, basically not expected to be used together/in the same way like topic words might be. further improvement could be by having a corpus of classical chinese works on this period, and getting the actual word embeddings so we know the word concept similarities and no longer assume independence of words i.e. the idea is to use soft cosine similarity instead of cosine similarity.



\>>> read_docs_into_dendrogram(bb, metric='cityblock') # this means manhattan distance for original documents

![image-20210907170431595](/Users/xingjing/Library/Application Support/typora-user-images/image-20210907170431595.png)



using manhattan distance gives even better results, but you need to explain why manhattan - which is why i didn't put this as default, though i think it should be. it might be harder to interpret for humanities people, but basically we don't assume that you can get the direct distance between two vectors (that sqrt(word^2 + word^2) is meaningful, for example). we assume the distance between two words (eg. word_a vs word_b) is exactly the presence/absence of word_a and word_b, and this can't be calculated as a difference in a shared scale. hence the huge distances as you sum up for manhattan distance all the presences/absences of the word. this is better for higher dimensional data.

\>>> read_docs_into_dendrogram(b, metric='cityblock')

![image-20210907171059059](/Users/xingjing/Library/Application Support/typora-user-images/image-20210907171059059.png)

manhattan distances, most common word only. my hypothesis is that hanfeizi and speaking to king in zheng are now less similiar because we CAN indeed assume that the words here are relatively more independent from each other, and treating them as axes make slightly more sense. and lower dimensional data, so euclidean distance doesnt suffer from curse of dimensionality as greatly.

