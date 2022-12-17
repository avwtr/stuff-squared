//
//  mainbtn.swift
//  trivia
//
//  Created by Alex Vawter on 12/16/22.
//

import SwiftUI

struct mainbtn: View {
    var text: String
    var backgrd: Color = Color("AccentColor")
    
    var body: some View {
        Text(text)
            .foregroundColor(.white)
            .padding()
            .padding(.horizontal)
            .background(backgrd)
            .cornerRadius(15)
            .shadow(radius: 10)
    }
}

struct mainbtn_Previews: PreviewProvider {
    static var previews: some View {
        mainbtn(text: "Next")
    }
}
