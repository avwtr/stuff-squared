//
//  questionV.swift
//  trivia
//
//  Created by Alex Vawter on 12/16/22.
//

import SwiftUI

struct questionV: View {
    @EnvironmentObject var triviaManager: TriviaManager
    var body: some View {
        VStack(spacing: 40){
            HStack{
                Text("Triviaverse").titleText()
                
                Spacer()
                
                Text("\(triviaManager.index + 1) out of \(triviaManager.length)").foregroundColor(Color("AccentColor"))
            }
            progV(progress: triviaManager.progress)
            
            VStack(alignment: .leading, spacing: 20){
                Text(triviaManager.question).font(.system(size: 20)).bold()
                    
                ForEach(triviaManager.answerChoices, id: \.id){
                    answer in anRow(answer: answer).environmentObject(triviaManager)
                }
                
            }
            
            
            Button {
                triviaManager.nextQuestion()
            } label: {
                mainbtn(text: "Onward", backgrd: triviaManager.answerSelected ?
                        Color("AccentColor"): Color(hue: 1.0, saturation: 0.0,
                                                    brightness: 0.564, opacity: 0.327))
                
            }.disabled(!triviaManager.answerSelected)
            
            Spacer()
            
        }.padding().frame(maxWidth: .infinity, maxHeight: .infinity).background(Color(red: 0.784 , green: 0.729, blue: 0.847))
            .navigationBarHidden(true)
    }
}

struct questionV_Previews: PreviewProvider {
    static var previews: some View {
        questionV().environmentObject(TriviaManager())
    }
}
