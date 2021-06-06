# -*- coding: UTF-8 -*-
from DataBaseOperator import DBConnector, DBOperate, DataBaseCreator
from DataGetter import ContentGetter, GetData, TitleGetter
from EmotionAnalysis import EmotionCounter
from FinanceDicBuilder import DicBuilder
from TextExtract import TextExtract

if __name__ == '__main__':
    dataGetter = GetData.GetData()
    dataGetter.getData()
    dicBuilder = DicBuilder.DicBuilder()
    dicBuilder.build_dic()
    emotionCounter = EmotionCounter.EmotionCounter()
    emotionCounter.generalize_emotion_report()
    times = 1
    while times <= 10:
        textExtract = TextExtract.TextExtract(times)
        times = textExtract.generate_report()

    print('ALL DONE!')
